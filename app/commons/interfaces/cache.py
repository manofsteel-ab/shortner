from abc import ABC, abstractmethod

class CacheInterface(ABC):

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass
