

from seedwork.domain.rules import BusinessRule


class DomainException(Exception):
    ...

class IdShouldBeInmutableExcepcion(DomainException):
    def __init__(self, mensaje='El identificador debe ser inmutable'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)

class BusinessRuleException(DomainException):
    def __init__(self, rule: BusinessRule):
        self.rule = rule

    def __str__(self):
        return str(self.rule)

class FactoryException(DomainException):
    def __init__(self, message):
        self.__message = message
    def __str__(self):
        return str(self.__message)