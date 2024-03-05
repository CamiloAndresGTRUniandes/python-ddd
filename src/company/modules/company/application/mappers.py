from seedwork.application.dto import Mapper as AppMap
from seedwork.domain.repositories import Mapper as RepMap
from modules.company.application.dto import CompanyDTO
from modules.company.domain.entities import Company
from seedwork.domain.value_objects import Money

class MapperCompanyDTOJson(AppMap):
    def external_to_dto(self, external: dict) -> CompanyDTO:
        company_dto = CompanyDTO()
        company_dto.name = external.get('name'),
        company_dto.price = external.get('price'),
        company_dto.currency = external.get('currency'),
        company_dto.seller = external.get('seller')
        return company_dto
    

    def dto_to_external(self, dto: CompanyDTO) -> dict:
        return dto.__dict__
    
class MapperCompany(RepMap):
    def get_type(self) -> type:
        return CompanyDTO.__class__

    def dto_to_entity(self, dto: CompanyDTO) -> Company:
        company_entity = Company()
        company_entity.name = dto.name
        company_entity.price = Money(dto.price, dto.currency)
        company_entity.seller = dto.seller
        return company_entity
    
    def entity_to_dto(self, entity: Company) -> CompanyDTO:
        company_dto = CompanyDTO()
        company_dto.id_company=entity.id,
        company_dto.name=entity.name,
        company_dto.price=entity.price.amount,
        company_dto.currency=entity.price.currency,
        company_dto.seller=entity.seller
    
    def entity_to_external(self, entity: Company) -> dict:
        return {
            "company_id" : f"{entity.id_company}",
            "name" : f"{entity.name}",
            "price" : entity.price.amount,
            "currency" : entity.price.currency,
            "created_at" : f"{entity.created_at}",
            "seller" : f"{entity.seller}"
        }
    
    def external_to_entity(self, external: dict) -> Company:
        company_entity = Company()
        company_entity.name= external.get('name')
        company_entity.price= Money(external.get('price'), external.get('currency'))
        company_entity.seller = external.get('seller')

        return company_entity
    