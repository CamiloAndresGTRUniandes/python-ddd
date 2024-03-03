

from dataclasses import dataclass
from modules.property.infrastructure.redis import RedisRepository
from seedwork.application.commands import Command, CommandHandler
from seedwork.domain.value_objects import Money
import uuid
import json
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
class CreateCacheProperty(Command):
    name: str = field(default_factory=str)
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)
    seller : str = field(default_factory=str)

class CreateCachePropertyHandler(CreatePropertyBaseHandler):
    def handle(self, command: CreateCacheProperty):
        property_dto = Property
        property_dto.name = command.name
        property_dto.price = Money(command.price, command.currency)
        property_dto.seller = command.seller

        map_property = MapperProperty()
        propertyJson = map_property.entity_to_external(property_dto)
        try:
            redis = RedisRepository()
            property_ext = json.dumps(propertyJson, indent = 4)
            redis.lpush("properties", property_ext)
        except Exception as e:
            print(e)
        

@command.register(CreateCacheProperty)
def execute_command_create_property(command: CreateCacheProperty):
    handler = CreateCachePropertyHandler()
    handler.handle(command)