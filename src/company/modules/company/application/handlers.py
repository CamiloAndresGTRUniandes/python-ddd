import logging
from seedwork.application.handlers import Handler
from modules.company.infrastructure.dispatchers import Dispatcher


class CompanyDomainHandler(Handler):

    @staticmethod
    def company_created_handler(event):
        try:
            dispatcher = Dispatcher()
            dispatcher.publish_event(event, 'companies-events')
        except Exception as e:
            logging.error(f"Publish error: {e}")
        