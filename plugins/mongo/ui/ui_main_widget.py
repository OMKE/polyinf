from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWidgetUI:

    def __init__(self, parent, parent_widget):
        self.parent = parent
        self.parent_widget = parent_widget
        self.main = QWidget(parent_widget)
        self.main.setObjectName("Mongo Widget")
        self.main.resize(903, 672)

        self.procedures_list = QListWidget(self.main)
        self.procedures_list.itemClicked.connect(self.procedure_clicked)
        self.fill_procedure_list(parent.get_procedures())
        self.procedures_list.setGeometry(QRect(30, 50, 181, 201))
        self.procedures_list.setObjectName("procedures_list")

        self.header_text = QLabel(self.main)
        self.header_text.setGeometry(QRect(30, 10, 181, 16))
        self.header_text.setObjectName("header_text")

        self.call_procedure_btn = QPushButton(self.main)
        self.call_procedure_btn.setGeometry(QRect(240, 90, 131, 32))
        self.call_procedure_btn.setObjectName("call_procedure_btn")

        self.procedure_param = QLineEdit(self.main)
        self.procedure_param.setGeometry(QRect(240, 50, 131, 21))
        self.procedure_param.setInputMethodHints(Qt.ImhNone)
        self.procedure_param.setObjectName("procedure_param")

        self.header_text_procedure_param = QLabel(self.main)
        self.header_text_procedure_param.setGeometry(QRect(240, 10, 131, 16))
        self.header_text_procedure_param.setObjectName("header_text_procedure_param")

        self.procedure_result = QTableView(self.main)
        self.procedure_result.setGeometry(QRect(420, 50, 1000, 600))
        self.procedure_result.setObjectName("procedure_result")

        self.header_text_procedure_param_2 = QLabel(self.main)
        self.header_text_procedure_param_2.setGeometry(QRect(420, 10, 131, 16))
        self.header_text_procedure_param_2.setObjectName("header_text_procedure_param_2")

        self.get_document_btn = QPushButton(self.main)
        self.get_document_btn.setGeometry(QRect(420, 700, 113, 32))
        self.get_document_btn.setObjectName("get_document_btn")

        QMetaObject.connectSlotsByName(self.main)

        self.header_text.setText('Procedures')
        self.call_procedure_btn.setText("Call procedure")
        self.header_text_procedure_param.setText("Procedure parameter")
        self.header_text_procedure_param_2.setText("Procedure result")
        self.get_document_btn.setText("Get document")


    def procedure_clicked(self, item):
        print(item.text())

    def widget(self):
        return self.main


    def fill_procedure_list(self, names:list):
        names.append('procedure_2')
        names.append('procedure_3')
        for name in names:
            self.procedures_list.addItem(name)
