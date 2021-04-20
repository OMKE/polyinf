from .plugin_interface import PluginInterface
from .plugin_specification import PluginSpecification


class Plugin(PluginInterface):

    def __init__(self, app, plugin_specification: PluginSpecification):
        super().__init__()
        self.app = app
        self._plugin_specification = plugin_specification

    def id(self) -> str:
        return self._plugin_specification.id()

    def name(self) -> str:
        return self._plugin_specification.name()

    def author(self) -> str:
        return self._plugin_specification.author()

    def description(self) -> str:
        return self._plugin_specification.description()

    def version(self) -> str:
        return self._plugin_specification.version()

    def release_notes(self) -> str:
        return self._plugin_specification.relase_notes()
