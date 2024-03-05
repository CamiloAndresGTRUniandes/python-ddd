from dataclasses import dataclass
from seedwork.application.commands import Command, CommandHandler
import uuid
from dataclasses import field
from modules.company.application.commands.base import CreateCompanyBaseHandler
from modules.company.application.dto import CompanyDTO

from modules.company.domain.entities import Company
from modules.company.application.mappers import MapperCompany
from modules.company.domain.repositories import CompanyRepository
from seedwork.application.commands import execute_command as command
from seedwork.infrastructure.unit_of_work import UnitOfWorkPort

import datetime

@dataclass
class CreateCompany(Command):
    name: str = field(default_factory=str)
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)
    seller : str = field(default_factory=str)

class CreateCompanyHandler(CreateCompanyBaseHandler):
    def handle(self, command: CreateCompany):
        company_dto = CompanyDTO()
        company_dto.name = command.name,
        company_dto.price = command.price,
        company_dto.currency = command.currency
        company_dto.seller = command.seller
            
        company : Company = self.companies_factory.create_object(company_dto, MapperCompany())
        company.create_company(company)
        repository = self.reposiroty_factory.create_object(CompanyRepository.__class__)
        UnitOfWorkPort.register_batch(repository.add, company)
        UnitOfWorkPort.commit()

@command.register(CreateCompany)
def execute_command_create_company(command: CreateCompany):
    handler = CreateCompanyHandler()
    handler.handle(command)