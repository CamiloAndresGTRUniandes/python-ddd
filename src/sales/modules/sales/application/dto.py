
from dataclasses import dataclass, field

from seedwork.application.dto import DTO


@dataclass
class PropertyDTO(DTO):
    id_property : str = field(default_factory=str)
    name: str = field(default_factory=str)
    price: str = field(default_factory=str)
    currency: str = field(default_factory=str)
    seller : str = field(default_factory=str)