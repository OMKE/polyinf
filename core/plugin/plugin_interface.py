from abc import ABC, abstractmethod


class PluginInterface(ABC):

    def __init__(self):
        super().__init__()

    def activate(self):
        raise NotImplementedError('Method must be implemented by a subclass')

    def deactivate(self):
        raise NotImplementedError('Method must be implemented by a subclass')

    @abstractmethod
    def widget(self, parent=None):
        raise NotImplementedError('Method must be implemented by a subclass')
