from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(69, 29, 501, 381))
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
        self.verticalLayout.addWidget(self.addDataBtn)
        self.addNewTableBtn = QPushButton(self.verticalLayoutWidget)
        self.addNewTableBtn.setObjectName("addNewTableBtn")
        self.verticalLayout.addWidget(self.addNewTableBtn)
        self.deleteDataBtn = QPushButton(self.verticalLayoutWidget)
        self.deleteDataBtn.setObjectName("deleteDataBtn")
        self.verticalLayout.addWidget(self.deleteDataBtn)
        self.modifyDataBtn = QPushButton(self.verticalLayoutWidget)
        self.modifyDataBtn.setObjectName("modifyDataBtn")
        self.verticalLayout.addWidget(self.modifyDataBtn)
        self.getDataBtn = QPushButton(self.verticalLayoutWidget)
        self.getDataBtn.setObjectName("getDataBtn")
        self.verticalLayout.addWidget(self.getDataBtn)
        self.retranslateUi(self)
        self.show()

    def retranslateUi(self, mainWidget):
        _translate = QCoreApplication.translate
        mainWidget.setWindowTitle(_translate("mainWidget", "Form"))
        self.label.setText(_translate(
            "mainWidget", "Dobrodošli na rad sa bazon"))
        self.addDataBtn.setText(_translate("mainWidget", "Dodavanje podataka"))
        self.addNewTableBtn.setText(_translate(
            "mainWidget", "Dodavanje nove tabele"))
        self.deleteDataBtn.setText(_translate(
            "mainWidget", "Brisanje podataka"))
        self.modifyDataBtn.setText(_translate("mainWidget", "Izmena podataka"))
        self.getDataBtn.setText(_translate(
            "mainWidget", "Dobavljanje podataka"))
