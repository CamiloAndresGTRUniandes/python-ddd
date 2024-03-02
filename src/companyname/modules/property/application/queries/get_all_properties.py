
from modules.property.application.queries.base import PropertyQueryBaseHandler
from seedwork.application.queries import Query, QueryHandler, QueryResult
from modules.property.domain.entities import Property
from modules.property.application.dto import PropertyDTO
from seedwork.application.queries import execute_query as query
from dataclasses import dataclass


@dataclass
class GetAllProperties(Query):
    ...


class GetAllPropertiesHandler(PropertyQueryBaseHandler):
    def handle(self, query) -> QueryResult:
        properties_dto = []
        view = self.view_factory.create_object(Property)
        properties = view.get_all()

        for property in properties:
            dto = PropertyDTO()
            dto.id = property.id
            dto.name = property.name
            dto.price = property.price
            dto.currency = property.currency
            dto.created_at = property.created_at
            properties_dto.append(dto)
        return QueryResult(properties_dto)
    
@query.register(GetAllProperties)
def ejecutar_query_obtener_propiedad(query: GetAllProperties):
    handler = GetAllPropertiesHandler()
    return handler.handle(query)