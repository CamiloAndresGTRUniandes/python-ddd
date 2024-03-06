from dataclasses import dataclass
from seedwork.domain.factory import Factory
from seedwork.domain.repositories import Mapper
from seedwork.domain.entities import Entity
from modules.sales.domain.entities import Sales


@dataclass
class PropertiesFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            sales: Sales = mapper.dto_to_entity(obj)
            return sales