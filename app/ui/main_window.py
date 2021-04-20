from PyQt5 import QtCore, QtGui, QtWidgets
from core.support.config.config_provider import ConfigProvider
from core.exceptions.exc import PluginNotFound


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.ui()

    def ui(self) -> None:
        self.setWindowTitle(ConfigProvider().name())
        self.setWindowIcon(QtGui.QIcon('resources/polyinf-logo.png'))
        self.showMaximized()
        self.status_bar = self.statusBar()
        self.menu_bar = QtWidgets.QMenuBar(self)

        self.populate_menu_bar()

    def set_central_widget(self, name: str):
        try:
            plugin = self.app.get('managers', 'PluginManager').get(name)
            widget = plugin.widget()[0]

            self.setCentralWidget(widget)
        except IndexError:
            raise PluginNotFound()

    def get_status_bar(self):
        return self.status_bar

    def populate_menu_bar(self) -> None:

        plugins_menu = QtWidgets.QMenu('&Plugins')

        plugins = self.app.get('managers', 'PluginManager').get_all()

        for i in plugins:
            plugins_menu.addAction(QtWidgets.QAction(
                QtGui.QIcon("resources/polyinf-logo.png"), "&New", self))

        self.menu_bar.addMenu(plugins_menu)
        self.setMenuBar(self.menu_bar)
