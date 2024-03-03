import json
from modules.property.application.queries.get_all_properties import GetAllProperties
import seedwork.presentation.api as api
from modules.property.application.mappers import MapperPropertyDTOJson
from modules.property.application.commands.create_property import CreateProperty
from seedwork.application.commands import execute_command
from seedwork.application.queries import execute_query

from flask import request, Response

from seedwork.domain.exceptions import DomainException


bp = api.create_blueprint('property', '/property')

@bp.route('', methods=['POST',])
def create_property():
    try:
        dict_property = request.json
        map_property = MapperPropertyDTOJson()
        property_dto = map_property.external_to_dto(dict_property)

        command = CreateProperty(
            name = property_dto.name,
            price = property_dto.price,
            currency = property_dto.currency,
            seller = property_dto.seller
        )
        execute_command(command)
        return Response('{}', status=202, mimetype='application/json')
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('', methods=('GET',))
def get_all_properties():
    map_property = MapperPropertyDTOJson()
    query_result = execute_query(GetAllProperties())
    results = []
    
    for propiedad in query_result.result:
        results.append(map_property.dto_to_external(propiedad))
    
    return results