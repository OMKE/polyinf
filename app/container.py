from abc import ABC
from core.exceptions.exc import ContainerEntityNotFoundException, ContainerKeyNotFound


class Container(ABC):

    def __init__(self):
        self.container = {
            'loggers': {},
            'managers': {},
            'parsers': {}
        }

    def bind(self, type_name, instance) -> None:
        try:
            self.container[type_name][type(instance).__name__] = instance
        except KeyError:
            raise ContainerKeyNotFound()

    def unbind(self, type_name, instance) -> None:
        del self.container[type_name][type(instance).__name__]

    def get(self, type, clazz) -> any:
        try:
            return self.container[type][clazz]
        except KeyError:
            raise ContainerEntityNotFoundException()

    def log(self, message: str, logger='SimpleLogger'):
        self.get('loggers', logger).log(message)
