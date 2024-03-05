from pulsar.schema import *
from dataclasses import dataclass, field
from seedwork.infrastructure.schema.v1.commands import (IntegrationCommand)

class CreateCompanyPayload(IntegrationCommand):
    seller = String()
    name= String()
    price= String()
    currency= String()
    created_at= String()

class CreateCompanyCommand(IntegrationCommand):
    data = CreateCompanyPayload()