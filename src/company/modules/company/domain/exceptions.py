

from seedwork.domain.exceptions import FactoryException


class ObjectTypeNotExistInCompanyDomainExeption(FactoryException):
    def __init__(self, message='There is not factory for this kind of entity'):
        self.__mensaje = message
    def __str__(self):
        return str(self.__mensaje)