from pydispatch import dispatcher
from .handlers import PropertyDomainHandler

dispatcher.connect(PropertyDomainHandler.property_created_handler, signal='PropertyCreatedDomain')
