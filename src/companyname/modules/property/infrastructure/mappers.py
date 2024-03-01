

from seedwork.application.dto import Mapper
from modules.property.domain.entities import Property
from .dto import Property as PropertyDTO



class PropertyMapper(Mapper):
    def entity_to_dto(self, entity: Property) -> PropertyDTO:
        property_dto = PropertyDTO(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            address=entity.address,
            price=entity.price,
            created_at=entity.created_at
        )
        return property_dto
    
    def dto_to_entity(self, dto: PropertyDTO) -> Property:
        property_entity = Property(
            id=dto.id,
            name=dto.name,
            description=dto.description,
            address=dto.address,
            price=dto.price,
            created_at=dto.created_at
        )
        return property_entity
    
    def get_type(self) -> type:
        return Property.__class__