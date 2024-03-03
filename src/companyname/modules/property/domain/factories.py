from dataclasses import dataclass
from seedwork.domain.factory import Factory
from seedwork.domain.repositories import Mapper
from seedwork.domain.entities import Entity
from modules.property.domain.entities import Property


@dataclass
class PropertiesFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            property: Property = mapper.dto_to_entity(obj)
            return property