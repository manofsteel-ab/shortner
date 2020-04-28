from flask import current_app
from redis import Redis

from app.commons.interfaces.cache import CacheInterface
from app.commons.interfaces.cache_factory import FactoryInterface

class RedisCache(CacheInterface):

    def __init__(self, host, port, db):
        self.db = Redis(
            host=host, port=port, db=db
        )

    def get(self, key):
        return self.db.get(key)

    def set(self, key, value):
        self.db.set(key,value)


class RedisCachFactory(FactoryInterface):

    def __init__(self):
        config = current_app.config
        self._cache = RedisCache(
            host=config.get('REDIS_HOST'),
            port=config.get('REDIS_PORT'),
            db=config.get('REDIS_CACHE_DB')
        )

    def get_cache(self):
        return self._cache
