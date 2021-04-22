from .container import Container
from .version import version
from .ui.main_window import MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from sys import exit
from core.support.config.config_provider import ConfigProvider


class Application(Container):
    def __init__(self, args):
        super().__init__()
        self.version = version()
        self._app = QtWidgets.QApplication(args)

    def main_window(self) -> None:
        self.main = MainWindow(self)
        return self.main

    def start(self) -> None:
        # Bind self to window so we have a refference to the container
        window = self.main_window()
        window.show()
        # Attach statusBar to SimpleLogger
        self.get('loggers', 'SimpleLogger').attach(self.main.get_status_bar())

        self.log(
            f'{ConfigProvider().name()} initialized. Version: {self.version}')

        exit(self._app.exec_())

    def app(self) -> QtWidgets.QApplication:
        return self._app

    def set_central_widget(self, widget):
        self.main.setCentralWidget(widget)
