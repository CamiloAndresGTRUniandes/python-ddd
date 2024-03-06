from config.db import db
from seedwork.infrastructure.uow_sales import UnitOfWork, Batch
import logging

class UnitOfWorkSQLAlchemySales(UnitOfWork):

    def __init__(self):
        self._batches: list[Batch] = list()

    def __enter__(self) -> UnitOfWork:
        return super().__enter__()

    def __exit__(self, *args):
        self.rollback()

    def _clear_batches(self):
        self._batches = list()

    @property
    def savepoints(self) -> list:
        return list[db.session.get_nested_transaction()]

    @property
    def batches(self) -> list[Batch]:
        return self._batches             

    def commit(self):
        try:
            for batch in self.batches:
                lock = batch.lock
                batch.operacion(*batch.args, **batch.kwargs)

            db.session.commit()

            super().commit()
        except Exception as e:
            logging.error(f"UOW ERROR: {e}")
    def rollback(self, savepoint=None):
        if savepoint:
            savepoint.rollback()
        else:
            db.session.rollback()
        
        super().rollback()
    
    def savepoint(self):
        db.session.begin_nested()