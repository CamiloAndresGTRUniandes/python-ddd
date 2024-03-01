


from dataclasses import dataclass

from seedwork.domain.events import DomainEvent


@dataclass
class PropertyCreated(DomainEvent):
    property_id: str
    name: str
    description: str
    price: float
    currency: str
    seller : str