from abc import ABC, abstractmethod

class BusinessRule(ABC):

    __message: str ='Invalid Business Rule'

    def __init__(self, mensaje):
        self.__message = mensaje

    def error_message(self) -> str:
        return self.__message

    @abstractmethod
    def is_valid(self) -> bool:
        ...

    def __str__(self):
        return f"{self.__class__.__name__} - {self.__message}"


class EntityIdIsInmutable(BusinessRule):

    entity: object

    def __init__(self, entity, message='Entity Id should be Inmutable'):
        super().__init__(message)
        self.entity = entity

    def is_valid(self) -> bool:
        try:
            if self.entity._id:
                return False
        except AttributeError as error:
            return True