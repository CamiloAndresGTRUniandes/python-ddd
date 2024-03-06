from seedwork.application.dto import Mapper as AppMap
from seedwork.domain.repositories import Mapper as RepMap
from modules.sales.application.dto import PropertyDTO
from modules.sales.domain.entities import Sales
from seedwork.domain.value_objects import Money

class MapperPropertyDTOJson(AppMap):
    def external_to_dto(self, external: dict) -> PropertyDTO:
        property_dto = PropertyDTO()
        property_dto.name = external.get('name'),
        property_dto.price = external.get('price'),
        property_dto.currency = external.get('currency'),
        property_dto.seller = external.get('seller')
        return property_dto
    

    def dto_to_external(self, dto: PropertyDTO) -> dict:
        return dto.__dict__
    
class MapperProperty(RepMap):
    def get_type(self) -> type:
        return PropertyDTO.__class__

    def dto_to_entity(self, dto: PropertyDTO) -> Sales:
        property_entity = Sales()
        property_entity.name = dto.name
        property_entity.price = Money(dto.price, dto.currency)
        property_entity.seller = dto.seller
        return property_entity
    
    def entity_to_dto(self, entity: Sales) -> PropertyDTO:
        property_dto = PropertyDTO()
        property_dto.id_property=entity.id,
        property_dto.name=entity.name,
        property_dto.price=entity.price.amount,
        property_dto.currency=entity.price.currency,
        property_dto.seller=entity.seller
    
    def entity_to_external(self, entity: Sales) -> dict:
        return {
            "property_id" : f"{entity.id_property}",
            "name" : f"{entity.name}",
            "price" : entity.price.amount,
            "currency" : entity.price.currency,
            "created_at" : f"{entity.created_at}",
            "seller" : f"{entity.seller}"
        }
    
    def external_to_entity(self, external: dict) -> Sales:
        property_entity = Sales()
        property_entity.name= external.get('name')
        property_entity.price= Money(external.get('price'), external.get('currency'))
        property_entity.seller = external.get('seller')

        return property_entity
    