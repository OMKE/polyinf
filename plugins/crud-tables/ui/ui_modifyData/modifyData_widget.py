from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ModifyData(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Form")
        self.resize(513, 394)
        self.label = QLabel(self)
        self.label.setGeometry(QRect(160, 10, 191, 51))
        self.label.setObjectName("label")
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(210, 320, 81, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(self)
        self.show()

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate(
            "Form", "Forma za izmenu podataka"))
        self.label.setText(_translate(
            "Form", "Forma za izmenu podataka"))
        self.pushButton.setText(_translate("Form", "Izmeni"))
