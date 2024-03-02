import pulsar
from pulsar.schema import *

import datetime
import json

from seedwork.infrastructure import utils
from modules.property.infrastructure.schema.v1.events import PropertyCreatedEvent, PropertyCreatedPayload
from modules.property.infrastructure.schema.v1.commands import CreatePropertyCommand, CreatePropertyPayload

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Dispatcher:
    def _publish_message(self, message, topic, schema):
        try:
            client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
            producer = client.create_producer(topic, schema=AvroSchema(PropertyCreatedEvent))
            producer.send(message)
            client.close()
        except Exception as ex:
            print(f' ERROR: {ex}')
            raise ex

    def publish_event(self, event, topic):
        payload = PropertyCreatedPayload(
            name = str(event.name),
            price=str(event.price),
            currency=str(event.currency),
            created_at=str(datetime.datetime.now())
        )
        integration_event = PropertyCreatedEvent(data= payload)
        self._publish_message(integration_event, topic, AvroSchema(PropertyCreatedEvent))

    def publish_command(self, command, topic):
        payload = CreatePropertyPayload(
            seller=command.seller,
            price=command.price,
            currency=command.currency,
            created_at=datetime.datetime.now(),
            name = command.name
        )
        integration_command = CreatePropertyPayload(data=payload)
        self._publish_message(integration_command, topic, AvroSchema(CreatePropertyCommand))
    