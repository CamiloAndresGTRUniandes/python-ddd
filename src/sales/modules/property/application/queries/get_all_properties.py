
from modules.sales.application.queries.base import PropertyQueryBaseHandler
from seedwork.application.queries import Query, QueryHandler, QueryResult
from modules.sales.domain.entities import Sales
from modules.sales.application.dto import PropertyDTO
from seedwork.application.queries import execute_query as query
from dataclasses import dataclass


@dataclass
class GetAllProperties(Query):
    ...


class GetAllPropertiesHandler(PropertyQueryBaseHandler):
    def handle(self, query) -> QueryResult:
        properties_dto = []
        view = self.view_factory.create_object(Sales)
        sales = view.get_all()

        for sales in sales:
            dto = PropertyDTO()
            dto.id = sales.id
            dto.name = sales.name
            dto.price = sales.price
            dto.currency = sales.currency
            dto.created_at = sales.created_at
            dto.seller = sales.seller
            properties_dto.append(dto)
        return QueryResult(properties_dto)
    
@query.register(GetAllProperties)
def ejecutar_query_obtener_propiedad(query: GetAllProperties):
    handler = GetAllPropertiesHandler()
    return handler.handle(query)