from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class AddDataWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def connect_to_db():
        raise NotImplementedError('Method not implemented')

    def get_db_data():
        raise NotImplementedError('Method not implemented')

    def initUI(self):
        self.setObjectName("Form")
        self.resize(747, 485)
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QRect(270, 10, 211, 71))
        self.comboBox.setObjectName("comboBox")
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(10, 100, 731, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.addDataLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.addDataLayout.setContentsMargins(0, 0, 0, 0)
        self.addDataLayout.setObjectName("addDataLayout")
        self.addBtn = QPushButton(self)
        self.addBtn.setGeometry(QRect(320, 420, 111, 41))
        self.addBtn.setObjectName("addBtn")

        self.retranslateUi(self)
        self.show()

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dodavanje podataka"))
        self.addBtn.setText(_translate("Form", "Dodaj podatak"))
