from core.support.foundation.manager import Manager
from core.plugin.plugin import Plugin
from json import load
from importlib import import_module
from inspect import getmembers, isclass
from core.plugin.plugin_specification import PluginSpecification
from core.plugin.plugin import Plugin
from core.support.config.config_provider import ConfigProvider
import os


class PluginManager(Manager):

    def __init__(self, app):
        super().__init__(app)
        self._plugins = {}

    def boot(self) -> None:
        self.install(ConfigProvider().plugins_path())

    def activate(self, plugin: Plugin) -> None:
        plugin.activate()
        self._plugins[plugin.id] = plugin

    def deactivate(self, plugin: Plugin) -> None:
        plugin.deactivate()
        del self._plugins[plugin.id]

    def install(self, path: str = 'plugins'):
        for directory in os.scandir(path):
            if directory.is_dir() and (directory.name != '__pycache__'):
                package_path = os.path.join(path, directory.name)
                plugin_path = os.path.join(package_path, 'plugin.py')
                spec_path = os.path.join(package_path, 'spec.json')
                with open(spec_path, 'r') as plugin_spec_file:
                    spec = load(plugin_spec_file)
                    # plugin_path = "/".join(plugin_path.split("/")[-3:-1])
                    plugin_module = import_module(
                        plugin_path.replace(os.path.sep, '.').rstrip('.py'))
                    class_members = getmembers(plugin_path, isclass)
                    if len(class_members) == 1:
                        plugin = plugin_module.Main(
                            self.app, PluginSpecification(spec))
                        self.activate(plugin)

    def uninstall(self, plugin: Plugin) -> None:
        return self.deactivate(plugin)

    def get(self, name: str) -> Plugin:
        return list(filter(lambda x: x._plugin_specification.name() == name, self._plugins))[0]

    def get_all(self):
        return self._plugins.values()
