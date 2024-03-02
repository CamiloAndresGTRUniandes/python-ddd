from seedwork.domain.exceptions import FactoryException

class NoExisteImplementacionParaTipoFabricaExcepcion(FactoryException):
    def __init__(self, message='Not Implemented.'):
        self.__message = message
    def __str__(self):
        return str(self.__message)