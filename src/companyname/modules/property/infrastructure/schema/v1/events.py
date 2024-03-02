from dataclasses import field
from pulsar.schema import *

from seedwork.infrastructure.schema.v1.events import IntegrationEvent

class PropertyCreatedPayload(Record):

    seller = String()
    name = String()
    price = String()
    currency = String()
    created_at = String()

    def to_json(self):
        return {
            "seller": self.seller,
            "name": self.name,
            "price": self.price,
            "currency": self.currency,
            "created_at": self.created_at
        }
    def create_event_payload(self, seller, name, price, currency, created_at):
        self.seller = seller
        self.name = name
        self.price = price
        self.currency = currency
        self.created_at = created_at
        

class PropertyCreatedEvent(IntegrationEvent):
    data = PropertyCreatedPayload()