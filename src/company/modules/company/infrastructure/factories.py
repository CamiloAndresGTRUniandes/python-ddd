


from dataclasses import dataclass
from modules.company.infrastructure.views import CompanyView
from seedwork.infrastructure.views import View
from modules.company.domain.entities import Company

from seedwork.domain.factory import Factory
from seedwork.domain.repositories import Repository
from modules.company.domain.repositories import CompanyRepository
from .repositories import PropertiesPostgresSQLRepository
from .exceptions import FactoryException


@dataclass
class ReposirotyFactory(Factory):
    def create_object(self, obj: type, mapper: any = None) -> Repository:
        if obj == CompanyRepository.__class__:
            return PropertiesPostgresSQLRepository()
        else:
            raise FactoryException(f"Error {obj}")
        
@dataclass
class ViewFactory(Factory):
    def create_object(self, obj: type, mapeador: any = None) -> View:
        if obj == Company:
            return CompanyView()
        else:
            raise FactoryException(f'Not Implemented {obj}')