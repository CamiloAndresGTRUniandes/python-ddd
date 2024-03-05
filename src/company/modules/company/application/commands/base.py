
from modules.company.infrastructure.factories import ReposirotyFactory 
from seedwork.application.commands import CommandHandler
from modules.company.domain.factories import PropertiesFactory


class CreateCompanyBaseHandler(CommandHandler):
    def __init__(self):
        self._reposiroty_factory: ReposirotyFactory = ReposirotyFactory()
        self._companies_factory: PropertiesFactory = PropertiesFactory()

    @property
    def reposiroty_factory(self):
        return self._reposiroty_factory
    
    @property
    def companies_factory(self):
        return self._companies_factory    
    