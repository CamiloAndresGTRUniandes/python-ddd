import datetime
import uuid
from seedwork.domain.entities import RootAggregation
from modules.property.domain.value_objects import Seller
from seedwork.domain.value_objects import Money
from dataclasses import dataclass, field
from modules.property.domain.events import PropertyCreated


@dataclass
class Property(RootAggregation):
    id_property: uuid.UUID = field(hash=True, default=uuid.uuid4())
    seller: str = field(default_factory=str)
    name: str = field(default_factory=str)
    price: Money = field(default_factory=Money)
    created_at: datetime = field(default_factory=datetime.datetime.now)

    def create_property(self, property : "Property"):
        self.name = property.name
        self.price = Money(amount=property.price.amount, currency=property.price.currency)
        self.seller = property.seller
        self.created_at = datetime.datetime.now()

        self.add_event(PropertyCreated(
            name = self.format_string(f"{self.name}"),
            price = self.format_string(f"{self.price.amount}"),
            currency =self.format_string(f"{self.price.currency}"),
            seller = self.seller
        ))
    def format_string(self, string : str):
        string = string.replace("(","")
        string = string.replace(")","")
        string = string.replace("'","")
        string = string.replace(",","")
        return string
