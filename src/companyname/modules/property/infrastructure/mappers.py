from seedwork.domain.repositories import Mapper
from modules.property.domain.entities import Property
from seedwork.domain.value_objects import Money
from .dto import Property as PropertyDTO



class PropertyMapper(Mapper):
    def entity_to_dto(self, entity: Property) -> PropertyDTO:
        property_dto = PropertyDTO()
        property_dto.id = entity.id,
        property_dto.name = entity.name
        property_dto.price = entity.price.amount,
        property_dto.currency = entity.price.currency,
        property_dto.created_at = entity.created_at,
        property_dto.seller = entity.seller
        return property_dto
    
    def dto_to_entity(self, dto: PropertyDTO) -> Property:
        property_entity = Property()
        property_entity.name = dto.name,
        property_entity.price = Money(dto.price, dto.currency)
        property_entity.seller = dto.seller
        return property_entity
    
    def get_type(self) -> type:
        return Property.__class__