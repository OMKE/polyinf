from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from core.plugin.plugin import Plugin
from core.plugin.plugin_guards import PluginGuards
from .ui.registration_form import RegistrationForm
from .ui.login_form import LoginForm

class Main(Plugin):
    def __init__(self, app, plugin_specification):
        super().__init__(app, plugin_specification)
        self.current_view = "login"

    def activate(self):
        self.app.log(f'{self.name()} activated')

    def deactivate(self):
        self.app.log(f'{self.name()} deactivated')

    def widget(self, parent=None):
        if self.current_view == "login":
            widget = LoginForm()
        else:
            widget = RegistrationForm()
        
        return widget

    def guard(self) -> str:
        return PluginGuards.NONE

