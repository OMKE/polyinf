from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from core.plugin.plugin import Plugin
from core.plugin.plugin_guards import PluginGuards
from .ui.homepage import Homepage


class Main(Plugin):
    def __init__(self, app, plugin_specification):
        super().__init__(app, plugin_specification)

    def activate(self):
        self.app.log(f'{self.name()} activated')

    def deactivate(self):
        self.app.log(f'{self.name()} deactivated')

    def widget(self, parent=None):
        widget = Homepage()
        widget.set_parent(self)
        return widget

    def logout(self):
        self.app.get('managers', 'AuthManager').logout()
        self.app.log('Logged out')

    def guard(self) -> str:
        return PluginGuards.AUTH

