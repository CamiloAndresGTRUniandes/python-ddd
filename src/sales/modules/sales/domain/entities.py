import datetime
import uuid
from seedwork.domain.entities import RootAggregation
from modules.sales.domain.value_objects import Seller
from seedwork.domain.value_objects import Money
from dataclasses import dataclass, field
from modules.sales.domain.events import PropertyCreated


@dataclass
class Sales(RootAggregation):
    id_property: uuid.UUID = field(hash=True, default=uuid.uuid4())
    seller: str = field(default_factory=str)
    name: str = field(default_factory=str)
    price: Money = field(default_factory=Money)
    created_at: datetime = field(default_factory=datetime.datetime.now)

    def create_property(self, sales : "Sales"):
        self.name = sales.name
        self.price = Money(amount=sales.price.amount, currency=sales.price.currency)
        self.seller = sales.seller
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
