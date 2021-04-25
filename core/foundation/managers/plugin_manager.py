from core.support.foundation.manager import Manager
from core.plugin.plugin_guards import PluginGuards
from json import load
from importlib import import_module
from inspect import getmembers, isclass
from core.plugin.plugin_specification import PluginSpecification
from core.plugin.plugin import Plugin
from core.support.config.config_provider import ConfigProvider
import os


class PluginManager(Manager):
    PIPELINE = {
        PluginGuards.AUTH,
        PluginGuards.NONE
    }

    def __init__(self, app):
        super().__init__(app)
        self._plugins = {}
        self._plugins_middleware = {}

    def __iter__(self):
        for plugin in self._plugins:
            yield plugin

    def set_pipeline(self):
        for plugin in self.get_all():
            self._plugins_middleware[plugin.name()] = plugin.guard()

    def set_central_widget(self, name=None):
        for middleware in self._plugins_middleware.items():
            if middleware[1] != self.get_pipeline('auth') and not self.app.get('managers', 'AuthManager').user():
                plugin_name = middleware[0]
                plugin = self.get(plugin_name)
                self.app.set_central_widget(plugin.widget())
            elif middleware[1] == self.get_pipeline('auth') and self.app.get('managers', 'AuthManager').user() and name:
                plugin_name = middleware[0]
                plugin = self.get(plugin_name)
                self.app.set_central_widget(plugin.widget())

    def get_pipeline(self, name) -> str:
        """
        Returns:
            string: if found returns pipe or None if not
        """
        for pipe in PluginManager.PIPELINE:
            if pipe == name:
                return pipe

    def boot(self) -> None:
        self.install(self.config_provider.plugins_path())

    def activate(self, plugin: Plugin) -> Plugin:
        plugin.activate()
        self._plugins[plugin.id] = plugin
        return plugin

    def deactivate(self, plugin: Plugin) -> Plugin:
        plugin.deactivate()
        del self._plugins[plugin.id]
        return plugin

    def install(self, path: str = 'plugins'):
        for directory in os.scandir(path):
            if directory.is_dir() and (directory.name != '__pycache__'):
                package_path = os.path.join(path, directory.name)
                plugin_path = os.path.join(package_path, 'plugin.py')
                spec_path = os.path.join(package_path, 'spec.json')
                with open(spec_path, 'r') as plugin_spec_file:
                    spec = load(plugin_spec_file)
                    icon_path = os.path.abspath(os.path.join(package_path, 'resources/icon.png'))
                    plugin_module = import_module(
                        plugin_path.replace(os.path.sep, '.').rstrip('.py'))
                    class_members = getmembers(plugin_path, isclass)
                    if len(class_members) == 1:
                        plugin = plugin_module.Main(
                            self.app, PluginSpecification(spec))
                        plugin.set_icon(icon_path)
                        self.activate(plugin)
        self.set_pipeline()

    def uninstall(self, plugin: Plugin) -> Plugin:
        return self.deactivate(plugin)

    def get(self, name: str) -> Plugin:
        return list(filter(lambda x: x.name() == name, self._plugins.values()))[0]

    def get_all(self):
        return self._plugins.values()
