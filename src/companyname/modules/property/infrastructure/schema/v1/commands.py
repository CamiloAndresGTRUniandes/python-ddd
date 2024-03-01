from pulsar.schema import *
from dataclasses import dataclass, field
from seedwork.infrastructure.schema.v1.commands import (IntegrationCommand)

class CreatePropertyPayload(IntegrationCommand):
    id_usuario = String()

class CreatePropertyCommand(IntegrationCommand):
    data = CreatePropertyPayload()