from seedwork.domain.repositories import Mapper
from modules.company.domain.entities import Company
from seedwork.domain.value_objects import Money
from .dto import Company as CompanyDTO



class CompanyMapper(Mapper):
    def entity_to_dto(self, entity: Company) -> CompanyDTO:
        company_dto = CompanyDTO()
        company_dto.id = entity.id,
        company_dto.name = entity.name
        company_dto.price = entity.price.amount,
        company_dto.currency = entity.price.currency,
        company_dto.created_at = entity.created_at,
        company_dto.seller = entity.seller
        return company_dto
    
    def dto_to_entity(self, dto: CompanyDTO) -> Company:
        company_entity = Company()
        company_entity.name = dto.name,
        company_entity.price = Money(dto.price, dto.currency)
        company_entity.seller = dto.seller
        return company_entity
    
    def get_type(self) -> type:
        return Company.__class__