from pulsar.schema import *
from dataclasses import dataclass, field
from seedwork.infrastructure.schema.v1.commands import (IntegrationCommand)

class CreatePropertyPayload(IntegrationCommand):
    seller = String()
    name= String()
    price= String()
    currency= String()
    created_at= String()

class CreatePropertyCommand(IntegrationCommand):
    data = CreatePropertyPayload()