import datetime
import uuid
from seedwork.domain.entities import RootAggregation
from modules.company.domain.value_objects import Seller
from seedwork.domain.value_objects import Money
from dataclasses import dataclass, field
from modules.company.domain.events import CompanyCreated


@dataclass
class Company(RootAggregation):
    id_company: uuid.UUID = field(hash=True, default=uuid.uuid4())
    seller: str = field(default_factory=str)
    name: str = field(default_factory=str)
    price: Money = field(default_factory=Money)
    created_at: datetime = field(default_factory=datetime.datetime.now)

    def create_company(self, company : "Company"):
        self.name = company.name
        self.price = Money(amount=company.price.amount, currency=company.price.currency)
        self.seller = company.seller
        self.created_at = datetime.datetime.now()

        self.add_event(CompanyCreated(
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
