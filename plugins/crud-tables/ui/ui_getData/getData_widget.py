from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class GetDataWidget(object):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Dobavi podatke")
        self.resize(400, 300)
        self.comboBox_2 = QComboBox(self)
        self.comboBox_2.setGeometry(QRect(230, 40, 131, 61))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QComboBox(self)
        self.comboBox_3.setGeometry(QRect(40, 40, 131, 61))
        self.comboBox_3.setObjectName("comboBox_3")
        self.getDataBtn = QPushButton(self)
        self.getDataBtn.setGeometry(QRect(150, 190, 101, 21))
        self.getDataBtn.setObjectName("getDataBtn")

        self.retranslateUi(self)
        self.show()

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dobavi podatke"))
        self.getDataBtn.setText(_translate("Dialog", "Dobavi podatke"))
