


from dataclasses import dataclass
from modules.property.infrastructure.views import PropertyView
from seedwork.infrastructure.views import View
from modules.property.domain.entities import Property

from seedwork.domain.factory import Factory
from seedwork.domain.repositories import Repository
from modules.property.domain.repositories import PropertyRepository
from .repositories import PropertiesPostgresSQLRepository
from .exceptions import FactoryException


@dataclass
class ReposirotyFactory(Factory):
    def create_object(self, obj: type, mapper: any = None) -> Repository:
        if obj == PropertyRepository.__class__:
            return PropertiesPostgresSQLRepository()
        else:
            raise FactoryException(f"Error {obj}")
        
@dataclass
class ViewFactory(Factory):
    def create_object(self, obj: type, mapeador: any = None) -> View:
        if obj == Property:
            return PropertyView()
        else:
            raise FactoryException(f'Not Implemented {obj}')