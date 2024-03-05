

import json
from seedwork.infrastructure.views import View
from .dto import Company as CompanyDTO
from .redis import RedisRepository




class CompanyView(View):
    def get_all(self):
        companies = list()
        redis = RedisRepository()
        propiedadesRedis = redis.lrange('companies', 0, -1)
        for companyRedis in propiedadesRedis:
            companyDto = json.loads(companyRedis)

            companies.append(CompanyDTO(
                name = companyDto['name'],
                price = companyDto['price'],
                currency = companyDto['currency'],
                seller = companyDto['seller'],
                created_at = companyDto['created_at']
                ))

        return companies
    
    def get_by(self, id=None, estado=None, id_cliente=None, **kwargs):
        raise NotImplementedError('Not Implemented')