from pulsar.schema import *
from dataclasses import dataclass, field
from seedwork.infrastructure.schema.v1.commands import (IntegrationCommand)

class CreatePropertyPayload(IntegrationCommand):
    seller: str
    name: str
    price: float
    currency: str
    created_at: str

class CreatePropertyCommand(IntegrationCommand):
    data = CreatePropertyPayload()