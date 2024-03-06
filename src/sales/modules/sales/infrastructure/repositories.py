from config.db import db
from modules.sales.domain.factories import PropertiesFactory
from modules.sales.domain.repositories import PropertyRepository
from modules.sales.domain.entities import Sales
from seedwork.domain.entities import Entity
from .mappers import PropertyMapper


class PropertiesPostgresSQLRepository(PropertyRepository):
    def __init__(self):
        self.properties_factory : PropertiesFactory = PropertiesFactory()

    def add(self, sales: Sales):
        property_dto = self.properties_factory.create_object(sales, PropertyMapper())
        db.session.add(property_dto)

    def get_all(self) -> list[Sales]:
        properties_dto = db.session.query(Sales).all()
        return properties_dto
    
    def get_by_id(self, id: int) -> Sales:
        property_dto = db.session.query(Sales).filter_by(id=id).first()
        return self.properties_factory.create_object(property_dto, PropertyMapper())
    
    def get_type(self) -> type:
        return Sales.__class__
    
    def delete(self, id: int):
        property_dto = db.session.query(Sales).filter_by(id=id).first()
        db.session.delete(property_dto)

    def update(self, entity: Entity):
        raise NotImplementedError
