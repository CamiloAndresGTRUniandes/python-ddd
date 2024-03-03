

import json
from seedwork.infrastructure.views import View
from .dto import Property as PropertyDTO
from .redis import RedisRepository




class PropertyView(View):
    def get_all(self):
        properties = list()
        redis = RedisRepository()
        propiedadesRedis = redis.lrange('properties', 0, -1)
        for propertyRedis in propiedadesRedis:
            propertyDto = json.loads(propertyRedis)

            properties.append(PropertyDTO(
                name = propertyDto['name'],
                price = propertyDto['price'],
                currency = propertyDto['currency'],
                seller = propertyDto['seller'],
                created_at = propertyDto['created_at']
                ))

        return properties
    
    def get_by(self, id=None, estado=None, id_cliente=None, **kwargs):
        raise NotImplementedError('Not Implemented')