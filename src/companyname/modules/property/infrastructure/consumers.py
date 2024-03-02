import json
import time
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback

from modules.property.application.commands.create_cache_property import CreateCacheProperty
from modules.property.infrastructure.schema.v1.commands import CreatePropertyCommand
from seedwork.application.commands import execute_command
from modules.property.infrastructure.schema.v1.events import PropertyCreatedEvent

from seedwork.infrastructure import utils

def subscribe_to_events():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('properties-events', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='properties-sub-events', schema=AvroSchema(PropertyCreatedEvent))
        
        while True:
            message = consumer.receive()
            ex = message.value()
            property_dto = ex.data
            print(f'EVENT RECEIVED: {property_dto}')
            command = CreateCacheProperty(
                name=property_dto,
                price=property_dto.price,
                currency=property_dto.currency,
                seller=property_dto.seller)
            execute_command(command)
            consumer.acknowledge(message)     

        client.close()
    except Exception as e:
        logging.error(f'ERROR: Subscribing to events topic!: {e}')
        traceback.print_exc()
        if client:
            client.close()

def subscribe_to_commands():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('property-commands', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='properties-sub-commands', schema=AvroSchema(CreatePropertyCommand))

        while True:
            message = consumer.receive()
            ex = message.value()
            property_dto = ex.data
            command = CreateCacheProperty(
                name=property_dto.name,
                price=property_dto.price,
                currency=property_dto.currency,
                seller=property_dto.seller
                )
            execute_command(command)
            consumer.acknowledge(message)     
            
        client.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if client:
            client.close()