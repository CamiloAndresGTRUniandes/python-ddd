
from modules.property.infrastructure.factories import ReposirotyFactory 
from seedwork.application.commands import CommandHandler
from modules.property.domain.factories import PropertiesFactory


class CreatePropertyBaseHandler(CommandHandler):
    def __init__(self):
        self._reposiroty_factory: ReposirotyFactory = ReposirotyFactory()
        self._properties_factory: PropertiesFactory = PropertiesFactory()

    @property
    def reposiroty_factory(self):
        return self._reposiroty_factory
    
    @property
    def properties_factory(self):
        return self._properties_factory    
    