from config.db import db
from modules.property.domain.factories import PropertiesFactory
from modules.property.domain.repositories import PropertyRepository
from modules.property.domain.entities import Property
from seedwork.domain.entities import Entity
from modules.property.infrastructure.mappers import PropertyMapper


class PropertiesPostgresSQLRepository(PropertyRepository):
    def __init__(self):
        self.properties_factory : PropertiesFactory = PropertiesFactory

    def add(self, property: Property):
        property_dto = self.properties_factory.create_object(property, PropertyMapper())
        db.session.add(property_dto)

    def get_all(self) -> list[Property]:
        properties_dto = db.session.query(Property).all()
        return properties_dto
    
    def get_by_id(self, id: int) -> Property:
        property_dto = db.session.query(Property).filter_by(id=id).first()
        return self.properties_factory.create_object(property_dto, PropertyMapper())
    
    def get_type(self) -> type:
        return Property.__class__
