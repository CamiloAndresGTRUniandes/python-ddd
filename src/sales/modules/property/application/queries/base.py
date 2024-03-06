
from modules.sales.infrastructure.factories import ViewFactory
from modules.sales.domain.factories import PropertiesFactory
from seedwork.application.queries import QueryHandler

class PropertyQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._view_factory: ViewFactory = ViewFactory()
        self._properties_factory: PropertiesFactory = PropertiesFactory()

    @sales
    def view_factory(self):
        return self._view_factory
    
    @sales
    def properties_factory(self):
        return self._properties_factory    