from dataclasses import dataclass, field

from seedwork.domain.events import (DomainEvent)


@dataclass
class PropertyCreated(DomainEvent):
    name : str = field(default_factory = str)
    description : str = field(default_factory = str)
    price : str = field(default_factory = str)
    currency : str = field(default_factory = str)
    seller : str = field(default_factory = str)
    created_at : str = field(default_factory = str)