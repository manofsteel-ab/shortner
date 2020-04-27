from abc import ABC, abstractmethod


class CronInterface(ABC):
    @abstractmethod
    def run(self):
        pass


class BaseCron(CronInterface):
    def run(self):
        pass
