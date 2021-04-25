from .container import Container
from .version import version
from .ui.main_window import MainWindow
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from sys import exit
from core.support.config.config_provider import ConfigProvider


class Application(Container):
    def __init__(self, args):
        super().__init__()
        self.version = version()
        self._app = QApplication(args)
        self.args = self.parse_args(args)

    def main_window(self) -> MainWindow:
        self.main = MainWindow(self)
        toolbar = self.main.addToolBar('Plugins')
        toolbar.setMovable(False)
        for action in self.set_toolbar_actions():
            toolbar.addAction(action)
        return self.main

    def set_toolbar_actions(self):
        actions = []
        for plugin in self.get('managers', 'PluginManager').get_all():
            if self.get('managers', 'AuthManager').user() and plugin.name() == 'AuthPlugin':
                continue
            action = QAction(QIcon(plugin.icon()), f'&{plugin.client_name()}', self.main)
            action.triggered.connect(lambda state, x=plugin: self.connect_action(x))
            actions.append(action)
        return actions

    def connect_action(self, plugin):
        self.get('managers', 'PluginManager').set_central_widget(plugin.widget())

    def start(self) -> None:
        if self.get_arg('--login'):
            self.get('managers', 'AuthManager').force_login()
        # Bind self to window so we have a refference to the container
        window = self.main_window()
        window.show()
        # Attach statusBar to SimpleLogger
        self.get('loggers', 'SimpleLogger').attach(self.main.get_status_bar())

        self.log(
            f'{ConfigProvider().name()} initialized. Version: {self.version}')

        self.get('managers', 'PluginManager').set_central_widget()

        exit(self._app.exec_())

    def app(self) -> QApplication:
        return self._app

    def set_central_widget(self, widget):
        self.main.setCentralWidget(widget)


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

