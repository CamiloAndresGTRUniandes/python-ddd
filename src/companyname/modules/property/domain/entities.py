

import dataclasses
import datetime
from seedwork.domain.entities import RootAggregation
from modules.property.domain.value_objects import Seller
from seedwork.domain.value_objects import Money
from dataclasses import field
from modules.property.domain.events import PropertyCreated


@dataclasses
class Property(RootAggregation):
    seller: Seller
    name: str = field(default_factory=str)
    price: Money
    created_at: datetime

    def create_property(self, name, price, currency, seller):
        self.name = name
        self.price = Money(amount=price, currency=currency)
        self.seller = Seller(seller)
        self.created_at = datetime.datetime.now()
        return self
    
    def add_event(self, event: PropertyCreated):
        return super().add_event(event)
