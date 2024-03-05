import json
from modules.company.application.queries.get_all_companies import GetAllProperties
import seedwork.presentation.api as api
from modules.company.application.mappers import MapperCompanyDTOJson
from modules.company.application.commands.create_company import CreateCompany
from seedwork.application.commands import execute_command
from seedwork.application.queries import execute_query

from flask import request, Response

from seedwork.domain.exceptions import DomainException


bp = api.create_blueprint('company', '/company')

@bp.route('', methods=['POST',])
def create_company():
    try:
        dict_company = request.json
        map_company = MapperCompanyDTOJson()
        company_dto = map_company.external_to_dto(dict_company)

        command = CreateCompany(
            name = company_dto.name,
            price = company_dto.price,
            currency = company_dto.currency,
            seller = company_dto.seller
        )
        execute_command(command)
        return Response('{}', status=202, mimetype='application/json')
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('', methods=('GET',))
def get_all_companies():
    map_company = MapperCompanyDTOJson()
    query_result = execute_query(GetAllProperties())
    results = []
    
    for propiedad in query_result.result:
        results.append(map_company.dto_to_external(propiedad))
    
    return results