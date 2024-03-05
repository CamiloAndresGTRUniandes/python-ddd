

from dataclasses import dataclass
from modules.company.infrastructure.redis import RedisRepository
from seedwork.application.commands import Command, CommandHandler
from seedwork.domain.value_objects import Money
import uuid
import json
from dataclasses import field
from modules.company.application.commands.base import CreateCompanyBaseHandler
from modules.company.application.dto import CompanyDTO

from modules.company.domain.entities import Company
from modules.company.application.mappers import MapperCompany
from modules.company.domain.repositories import CompanyRepository
from seedwork.application.commands import execute_command as command
from seedwork.infrastructure.unit_of_work import UnitOfWorkPortCompany

import datetime

@dataclass
class CreateCacheCompany(Command):
    name: str = field(default_factory=str)
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)
    seller : str = field(default_factory=str)

class CreateCacheCompanyHandler(CreateCompanyBaseHandler):
    def handle(self, command: CreateCacheCompany):
        company_dto = Company
        company_dto.name = command.name
        company_dto.price = Money(command.price, command.currency)
        company_dto.seller = command.seller

        map_company = MapperCompany()
        companyJson = map_company.entity_to_external(company_dto)
        try:
            redis = RedisRepository()
            company_ext = json.dumps(companyJson, indent = 4)
            redis.lpush("companies", company_ext)
        except Exception as e:
            print(e)
        

@command.register(CreateCacheCompany)
def execute_command_create_company(command: CreateCacheCompany):
    handler = CreateCacheCompanyHandler()
    handler.handle(command)