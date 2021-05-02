from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from core.plugin.plugin import Plugin
from core.plugin.plugin_guards import PluginGuards
from .widget import MainWidget
from .utils.mongo_logger import MongoPluginLogger

class Main(Plugin):
    def __init__(self, app, plugin_specification):
        super().__init__(app, plugin_specification)

    def activate(self):
        self.app.log(f'{self.name()} activated')
        self.app.bind('loggers', MongoPluginLogger())

    def deactivate(self):
        self.app.log(f'{self.name()} deactivated')

    def widget(self, parent=None):
        main_widget = MainWidget(self, self.app)
        return main_widget.widget()

    def guard(self) -> str:
        return PluginGuards.AUTH

