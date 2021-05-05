from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from .ui_getData.getData_widget import GetDataWidget

def getData():
    getData_widget = GetDataWidget()
    getData_widget.exec_()

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
        self.getDataBtn.setText(_translate(
            "mainWidget", "Dobavljanje podataka"))
