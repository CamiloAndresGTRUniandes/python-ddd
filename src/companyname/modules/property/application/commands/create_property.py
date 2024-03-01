

from dataclasses import dataclass
from seedwork.application.commands import Command, CommandHandler
import uuid
from dataclasses import field
from modules.property.application.commands.base import CreatePropertyBaseHandler
from modules.property.application.dto import PropertyDTO

from modules.property.domain.entities import Property
from modules.property.infrastructure.mappers import PropertyMapper
from modules.property.domain.repositories import PropertyRepository
from seedwork.application.commands import execute_command as command

@dataclass
class CreateProperty(Command):
    id: str = field(default_factory=str)
    name: str = field(default_factory=str)
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)

class CreatePropertyHandler(CreatePropertyBaseHandler):
    def handle(self, command: CreateProperty):
        property_dto = PropertyDTO(
            id=command.id,
            name=command.name,
            price=command.price,
            currency=command.currency,
            seller=command.seller,
            created_at=command.created_at)
            
        property : Property = self.properties_factory.create_object(property_dto, PropertyMapper())
        property.create_property(property)

        repository = self.reposiroty_factory.create_object(PropertyRepository.__class__)


@command.register(CreateProperty)
def ejecutar_comando_crear_reserva(command: CreateProperty):
    handler = CreatePropertyHandler()
    handler.handle(command)