import logging
from seedwork.application.handlers import Handler
from modules.property.infrastructure.dispatchers import Dispatcher


class PropertyDomainHandler(Handler):

    @staticmethod
    def property_created_handler(event):
        try:
            dispatcher = Dispatcher()
            dispatcher.publish_command(event, 'property_commands')
        except Exception as e:
            logging.error(f"Publish error: {e}")
        