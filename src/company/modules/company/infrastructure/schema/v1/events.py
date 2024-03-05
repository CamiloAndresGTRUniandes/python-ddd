from dataclasses import field
from pulsar.schema import *

from seedwork.infrastructure.schema.v1.events import IntegrationEvent

class CompanyCreatedPayload(Record):

    seller = String()
    name = String()
    price = String()
    currency = String()
    created_at = String()

class CompanyCreatedEvent(IntegrationEvent):
    data = CompanyCreatedPayload()