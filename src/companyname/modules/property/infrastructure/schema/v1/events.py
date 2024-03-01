from pulsar.schema import *

from seedwork.infrastructure.schema.v1.events import IntegrationEvent

class PropertyCreatedPayload(Record):
    seller: str
    name: str
    price: float
    currency: str
    created_at: str

class PropertyCreatedEvent(IntegrationEvent):
    data = PropertyCreatedPayload()