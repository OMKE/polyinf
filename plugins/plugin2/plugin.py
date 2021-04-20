from PyQt5 import QtCore, QtGui, QtWidgets
from core.plugin.plugin import Plugin


class Main(Plugin):

    def __init__(self, app, plugin_specification):
        super().__init__(app, plugin_specification)

    def activate(self):
        print('activated')

    def deactivate(self):
        print('deactivated')

    def widget(self, parent=None):
        widget = QtWidgets.QComboBox()
        widget.setObjectName('combo')
        widget.addItem('str 1')
        widget.addItem('str 2')
        widget.addItem('str 3')
        return widget
