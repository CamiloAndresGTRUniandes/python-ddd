from config.db import db
from modules.company.domain.factories import PropertiesFactory
from modules.company.domain.repositories import CompanyRepository
from modules.company.domain.entities import Company
from seedwork.domain.entities import Entity
from .mappers import CompanyMapper


class PropertiesPostgresSQLRepository(CompanyRepository):
    def __init__(self):
        self.companies_factory : PropertiesFactory = PropertiesFactory()

    def add(self, company: Company):
        company_dto = self.companies_factory.create_object(company, CompanyMapper())
        db.session.add(company_dto)

    def get_all(self) -> list[Company]:
        companies_dto = db.session.query(Company).all()
        return companies_dto
    
    def get_by_id(self, id: int) -> Company:
        company_dto = db.session.query(Company).filter_by(id=id).first()
        return self.companies_factory.create_object(company_dto, CompanyMapper())
    
    def get_type(self) -> type:
        return Company.__class__
    
    def delete(self, id: int):
        company_dto = db.session.query(Company).filter_by(id=id).first()
        db.session.delete(company_dto)

    def update(self, entity: Entity):
        raise NotImplementedError
