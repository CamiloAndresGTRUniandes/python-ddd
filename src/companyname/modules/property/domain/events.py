from dataclasses import dataclass

from seedwork.domain.events import (DomainEvent)


@dataclass
class PropertyCreated(DomainEvent):
    name: str = None
    description: str = None
    price: float = None
    currency: str = None
    seller : str = None