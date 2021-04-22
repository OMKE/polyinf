from PyQt5 import QtCore, QtGui, QtWidgets
from core.plugin.plugin import Plugin


class Main(Plugin):
    def __init__(self, app, plugin_specification):
        super().__init__(app, plugin_specification)

    def activate(self):
        self.app.log(f'{self.name()} activated')

    def deactivate(self):
        self.app.log(f'{self.name()} deactivated')

    def widget(self, parent=None):
        widget = QtWidgets.QComboBox()
        widget.setObjectName('combo')
        widget.addItem('text 1')
        widget.addItem('text 2')
        widget.addItem('text 3')
        return widget
