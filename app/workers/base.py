from abc import ABC, abstractmethod


class WorkerInterface(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def process(self, message, retry=0):
        pass


class BaseWorker(WorkerInterface):

    def start(self):
        pass

    def process(self, message, retry=0):
        pass
