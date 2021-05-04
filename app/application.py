from .container import Container
from .version import version
from .ui.main_window import MainWindow
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from sys import exit
from core.support.config.config_provider import ConfigProvider
from PyQt5 import QtWebEngineWidgets

class Application(Container):
    def __init__(self, args):
        super().__init__()
        self.version = version()
        self._app = QApplication(args)
        self.args = self.parse_args(args)

    def main_window(self) -> MainWindow:
        self.main = MainWindow(self)
        self.toolbar = self.main.addToolBar('Plugins')
        self.toolbar.setMovable(False)
        self.add_toolbar_actions(self.get_toolbar_actions())
        return self.main

    def add_toolbar_actions(self, actions):
        for action in actions:
            self.toolbar.addAction(action['action'])

    def get_toolbar_actions(self):
        actions = []
        for plugin in self.get('managers', 'PluginManager').get_all():
            if self.get('managers', 'AuthManager').user() and plugin.name() == 'AuthPlugin':
                continue
            action = QAction(QIcon(plugin.icon()), f'&{plugin.client_name()}', self.main)
            action.triggered.connect(lambda state, x=plugin: self.connect_action(x))
            actions.append({
                "plugin": plugin.name(),
                "action": action
            })
        return actions

    def refresh_actions(self):
        actions = []
        for i, v in enumerate(self.toolbar.actions()):
            if i == 1 or i == 2 and self.get('managers', 'AuthManager').user().get_role() == 'user':
                actions.append(v)
        for action in actions:
            action.setDisabled(True)
            action.deleteLater()



    def connect_action(self, plugin):
        self.get('managers', 'PluginManager').set_central_widget(plugin.widget())

    def refresh(self):
        self.refresh_actions()

    def start(self) -> None:
        if ConfigProvider().development():
            if self.get_arg('--login'):
                role = self.get_arg('--role')
                if role:
                    self.get('managers', 'AuthManager').force_login(role)
                else:
                    self.get('managers', 'AuthManager').force_login()

        window = self.main_window()
        window.show()

        # Attach all loggers to Status Bar
        self.attach_loggers_to_status_bar(self.container['loggers'])

        self.log(
            f'{ConfigProvider().name()} initialized. Version: {self.version}')

        self.get('managers', 'PluginManager').set_central_widget()

        exit(self._app.exec_())

    def app(self) -> QApplication:
        return self._app

    def set_central_widget(self, widget):
        self.main.setCentralWidget(widget)

    def get_central_widget(self):
        return self.main.centralWidget()

    def parse_args(self, args):
        args = [{'name': arg.split("=")[0], "value": arg.split("=")[1]} for arg in args[1:] if "=" in arg]
        return args

    def get_arg(self, arg_name):
        for arg in self.args:
            try:
                if arg['name'] == arg_name:
                    return arg['value']
            except KeyError:
                return None

    def attach_loggers_to_status_bar(self, loggers):
        for logger in loggers:
            self.get('loggers', logger).attach(self.main.get_status_bar())
