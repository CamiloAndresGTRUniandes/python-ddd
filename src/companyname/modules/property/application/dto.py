
from dataclasses import dataclass

from seedwork.application.dto import DTO


@dataclass
class PropertyDTO(DTO):
    name: str
    type: str
    price: str
    currency: str
    created_at: str