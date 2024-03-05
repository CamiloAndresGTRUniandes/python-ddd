
from modules.company.infrastructure.factories import ViewFactory
from modules.company.domain.factories import PropertiesFactory
from seedwork.application.queries import QueryHandler

class CompanyQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._view_factory: ViewFactory = ViewFactory()
        self._companies_factory: PropertiesFactory = PropertiesFactory()

    @property
    def view_factory(self):
        return self._view_factory
    
    @property
    def companies_factory(self):
        return self._companies_factory    