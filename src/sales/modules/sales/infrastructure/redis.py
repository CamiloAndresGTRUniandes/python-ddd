import redis
import os
from seedwork.infrastructure.utils import redis_host

class RedisRepository:
    def __init__(self):
        self.cx=redis.Redis(host=redis_host())

    def lrange(self, key, start, end):
        return self.cx.lrange(key, start, end)
    
    def linsert(self, key, where, pivot, value):
        return self.cx.linsert(key, where, pivot, value)

    def lpush(self, key, value):
        return self.cx.lpush(key, value)
    
    def getAll(self, key):
        return self.cx.lrange(key, 0, -1)
    
    