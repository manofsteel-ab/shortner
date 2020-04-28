from app.commons.services.cache.redis_cache_factory import RedisCachFactory

class Singleton(type):
    _shared_state = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._shared_state:
            cls._shared_state[cls] = super(Singleton, cls).__call__(
                *args, **kwargs
            )
        return cls._shared_state[cls]

class Cache(metaclass=Singleton):

    def __init__(self):
        self.current_factory = RedisCachFactory()

    def get_instance(self):
        return self.current_factory.get_cache()
