from abc import ABC, abstractmethod


class LoggerInterface(ABC):

    @abstractmethod
    def log(self, message: str):
        raise NotImplementedError('Method must be implemented by a subclass')
