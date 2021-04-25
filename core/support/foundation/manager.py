from abc import ABC, abstractmethod
from collections.abc import Callable
from core.support.config.config_provider import ConfigProvider


class Manager(ABC):

    def __init__(self, app):
        self.app = app
        self.booting_callbacks = []
        self.booted_callbacks = []
        self.config_provider = ConfigProvider()

    @abstractmethod
    def boot(self) -> None:
        raise NotImplementedError('Method must be implemented by a subclass')

    """ Add callback to be called before manager is booted """

    def booting(self, callback: Callable) -> None:
        self.booting_callbacks.append(callback)

    """ Add callback to be called after manager is booted """

    def booted(self, callback: Callable) -> None:
        self.booted_callbacks.append(callback)

    """ Calls provided callbacks before manager is booted """

    def call_booting_callbacks(self) -> None:
        for callback in self.booting_callbacks:
            callback()

    """ Calls provided callbacks after manager is booted """

    def call_booted_callbacks(self) -> None:
        for callback in self.booted_callbacks:
            callback()
