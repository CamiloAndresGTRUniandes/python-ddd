from dataclasses import dataclass
from seedwork.application.commands import Command, CommandHandler
import uuid
from dataclasses import field
from modules.property.application.commands.base import CreatePropertyBaseHandler
from modules.property.application.dto import PropertyDTO

from modules.property.domain.entities import Property
from modules.property.application.mappers import MapperProperty
from modules.property.domain.repositories import PropertyRepository
from seedwork.application.commands import execute_command as command
from seedwork.infrastructure.uow import UnitOfWorkPort

import datetime

@dataclass
class CreateProperty(Command):
    name: str = field(default_factory=str)
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)
    seller : str = field(default_factory=str)

class CreatePropertyHandler(CreatePropertyBaseHandler):
    def handle(self, command: CreateProperty):
        property_dto = PropertyDTO()
        property_dto.name = command.name,
        property_dto.price = command.price,
        property_dto.currency = command.currency
        property_dto.seller = command.seller
            
        property : Property = self.properties_factory.create_object(property_dto, MapperProperty())
        property.create_property(property)
        repository = self.reposiroty_factory.create_object(PropertyRepository.__class__)
        UnitOfWorkPort.register_batch(repository.add, property)
        UnitOfWorkPort.commit()

@command.register(CreateProperty)
def execute_command_create_property(command: CreateProperty):
    handler = CreatePropertyHandler()
    handler.handle(command)