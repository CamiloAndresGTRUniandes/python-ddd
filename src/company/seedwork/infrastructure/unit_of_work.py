from abc import ABC, abstractmethod
from enum import Enum

from seedwork.domain.entities import RootAggregation
from pydispatch import dispatcher

import pickle


class Lock(Enum):
    OPTIMISTA = 1
    PESIMISTA = 2

class Batch:
    def __init__(self, operacion, lock: Lock, *args, **kwargs):
        self.operacion = operacion
        self.args = args
        self.lock = lock
        self.kwargs = kwargs

class UnitOfWork(ABC):

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    def _get_events(self, batches=None):
        batches = self.batches if batches is None else batches
        for batch in batches:
            for arg in batch.args:
                if isinstance(arg, RootAggregation):
                    return arg.events
        return list()

    @abstractmethod
    def _clear_batches(self):
        raise NotImplementedError

    @abstractmethod
    def batches(self) -> list[Batch]:
        raise NotImplementedError

    @abstractmethod
    def savepoints(self) -> list:
        raise NotImplementedError                    

    def commit(self):
        self._publish_events_post_commit()
        self._clear_batches()

    @abstractmethod
    def rollback(self, savepoint=None):
        self._clear_batches()
    
    @abstractmethod
    def savepoint(self):
        raise NotImplementedError

    def register_batch(self, operation, *args, lock=Lock.PESIMISTA, **kwargs):
        batch = Batch(operation, lock, *args, **kwargs)
        self.batches.append(batch)
        self._publish_domain_events(batch)

    def _publish_domain_events(self, batch):
        for event in self._get_events(batches=[batch]):
            dispatcher.send(signal=f'{type(event).__name__}Domain', event=event)

    def _publish_events_post_commit(self):
        for event in self._get_events():
            dispatcher.send(signal=f'{type(event).__name__}Integration', event=event)

def is_flask():
    try:
        from flask import session
        return True
    except Exception as e:
        return False

def register_unit_of_work(serialized_obj):
    from config.unit_of_work import UnitOfWorkSQLAlchemyCompany
    from flask import session
    

    session['unit_of_work'] = serialized_obj

def flask_unit_of_work():
    from flask import session
    from config.unit_of_work import UnitOfWorkSQLAlchemyCompany
    if session.get('unit_of_work'):
        return session['unit_of_work']
    else:
        unit_of_work_serialized = pickle.dumps(UnitOfWorkSQLAlchemyCompany())
        register_unit_of_work(unit_of_work_serialized)
        return unit_of_work_serialized

def unit_of_work() -> UnitOfWork:
    if is_flask():
        return pickle.loads(flask_unit_of_work())
    else:
        raise Exception('There is not unit of work')

def save_unit_of_work(unit_of_work: UnitOfWork):
    if is_flask():
        register_unit_of_work(pickle.dumps(unit_of_work))
    else:
        raise Exception('There is not unit of work')


class UnitOfWorkPortCompany:

    @staticmethod
    def commit():
        unit_of_work = unit_of_work()
        unit_of_work.commit()
        save_unit_of_work(unit_of_work)

    @staticmethod
    def rollback(savepoint=None):
        unit_of_work = unit_of_work()
        unit_of_work.rollback(savepoint=savepoint)
        save_unit_of_work(unit_of_work)

    @staticmethod
    def savepoint():
        unit_of_work = unit_of_work()
        unit_of_work.savepoint()
        save_unit_of_work(unit_of_work)

    @staticmethod
    def dar_savepoints():
        unit_of_work = unit_of_work()
        return unit_of_work.savepoints()

    @staticmethod
    def register_batch(operation, *args, lock=Lock.PESIMISTA, **kwargs):
        unit_of_work = unit_of_work()
        unit_of_work.register_batch(operation, *args, lock=lock, **kwargs)
        save_unit_of_work(unit_of_work)
