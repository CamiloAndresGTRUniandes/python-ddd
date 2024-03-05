
from dataclasses import dataclass, field

from seedwork.application.dto import DTO


@dataclass
class CompanyDTO(DTO):
    id_company : str = field(default_factory=str)
    name: str = field(default_factory=str)
    price: str = field(default_factory=str)
    currency: str = field(default_factory=str)
    seller : str = field(default_factory=str)