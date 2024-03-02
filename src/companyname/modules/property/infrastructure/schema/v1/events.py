from dataclasses import field
from pulsar.schema import *

from seedwork.infrastructure.schema.v1.events import IntegrationEvent

class PropertyCreatedPayload(Record):

    seller = String()
    name = String()
    price = String()
    currency = String()
    created_at = String()

class PropertyCreatedEvent(IntegrationEvent):
    data = PropertyCreatedPayload()