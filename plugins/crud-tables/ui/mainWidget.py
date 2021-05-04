from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from .ui_getData.getData_widget import GetDataWidget
from .ui_addData.addData_widget import AddDataWidget
from .ui_addTable.addNewTable_widget import AddNewTable
from .ui_modifyData.modifyData_widget import ModifyData


def getData():
    getData_widget = GetDataWidget()
    getData_widget.exec_()


def modifyData():
    modifyData_widget = ModifyData()
    modifyData_widget.exec_()


def addData():
    addData_widget = AddDataWidget()
    addData_widget.exec_()


def addTable():
    addTable_wdiget = AddNewTable()
    addTable_wdiget.exec_()


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(50, 50, 350, 350))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)
        self.addDataBtn = QPushButton(self.verticalLayoutWidget)
        self.addDataBtn.setObjectName("addDataBtn")
        self.addDataBtn.clicked.connect(addData)

        self.verticalLayout.addWidget(self.addDataBtn)
        self.addNewTableBtn = QPushButton(self.verticalLayoutWidget)
        self.addNewTableBtn.setObjectName("addNewTableBtn")
        self.verticalLayout.addWidget(self.addNewTableBtn)
        self.addNewTableBtn.clicked.connect(addTable)

        self.modifyDataBtn = QPushButton(self.verticalLayoutWidget)
        self.modifyDataBtn.setObjectName("modifyDataBtn")
        self.verticalLayout.addWidget(self.modifyDataBtn)
        self.modifyDataBtn.clicked.connect(modifyData)

        self.getDataBtn = QPushButton(self.verticalLayoutWidget)
        self.getDataBtn.setObjectName("getDataBtn")
        self.verticalLayout.addWidget(self.getDataBtn)
        self.getDataBtn.clicked.connect(getData)

        self.retranslateUi(self)
        self.show()

    def retranslateUi(self, mainWidget):
        _translate = QCoreApplication.translate
        mainWidget.setWindowTitle(_translate("mainWidget", "Form"))
        self.label.setText(_translate(
            "mainWidget", "Dobrodošli na rad sa bazom"))
        self.addDataBtn.setText(_translate("mainWidget", "Dodavanje podataka"))
        self.addNewTableBtn.setText(_translate(
            "mainWidget", "Dodavanje nove tabele"))
        self.modifyDataBtn.setText(_translate("mainWidget", "Izmena podataka"))
        self.getDataBtn.setText(_translate(
            "mainWidget", "Dobavljanje podataka"))
