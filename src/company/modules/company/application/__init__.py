from pydispatch import dispatcher
from .handlers import CompanyDomainHandler

dispatcher.connect(CompanyDomainHandler.company_created_handler, signal='CompanyCreatedDomain')
