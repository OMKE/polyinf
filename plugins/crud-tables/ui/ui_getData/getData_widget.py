from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class GetDataWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Form")
        self.resize(400, 300)
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QRect(30, 20, 141, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox1 = QComboBox(self)
        self.comboBox1.setGeometry(QRect(230, 20, 151, 31))
        self.comboBox1.setObjectName("comboBox1")
        self.getDataBtn = QPushButton(self)
        self.getDataBtn.setGeometry(QRect(150, 90, 111, 41))
        self.getDataBtn.setObjectName("getDataBtn")
        self.dataLabel = QLabel(self)
        self.dataLabel.setGeometry(QRect(70, 170, 271, 51))
        self.dataLabel.setText("")
        self.dataLabel.setObjectName("dataLabel")

        self.retranslateUi(self)
        self.show()

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Forma za dobavljanje podataka"))
        self.getDataBtn.setText(_translate("Form", "Dobavi podatke"))
