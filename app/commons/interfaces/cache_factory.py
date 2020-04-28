from abc import ABC, abstractmethod


class FactoryInterface(ABC):

    @abstractmethod
    def get_cache(self):
        pass
