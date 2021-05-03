from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWidgetUI:

    def __init__(self, parent, parent_widget):
        self.parent = parent
        self.parent_widget = parent_widget
        self.main = QWidget(parent_widget)
        self.main.setObjectName("Mongo Widget")
        self.main.resize(903, 672)
        self.current_procedure = {}
        self.open_in_browser = False

        self.procedures_list = QListWidget(self.main)
        self.procedures_list.itemClicked.connect(self.procedure_clicked)
        self.fill_procedure_list(parent.get_procedures())
        self.procedures_list.setGeometry(QRect(30, 50, 181, 201))
        self.procedures_list.setObjectName("procedures_list")

        self.documents_list = QListWidget(self.main)
        self.documents_list.itemDoubleClicked.connect(self.document_clicked)
        self.sync_document_list()
        self.documents_list.setGeometry(QRect(30, 300, 350, 600))
        self.documents_list.setObjectName("document_list")

        # Procedures text
        self.header_text = QLabel(self.main)
        self.header_text.setGeometry(QRect(30, 10, 181, 16))
        self.header_text.setObjectName("header_text")

        # Procedure parameter text
        self.header_text_procedure_param = QLabel(self.main)
        self.header_text_procedure_param.setGeometry(QRect(240, 10, 131, 16))
        self.header_text_procedure_param.setObjectName("header_text_procedure_param")

        # Procedure result text
        self.header_text_procedure_param_2 = QLabel(self.main)
        self.header_text_procedure_param_2.setGeometry(QRect(420, 10, 131, 16))
        self.header_text_procedure_param_2.setObjectName("header_text_procedure_param_2")

        # Document text
        self.header_text_documents = QLabel(self.main)
        self.header_text_documents.setGeometry(QRect(30, 270, 131, 16))
        self.header_text_documents.setObjectName("header_text_documents")

        # Call procedure button
        self.call_procedure_btn = QPushButton(self.main)
        self.call_procedure_btn.setGeometry(QRect(240, 90, 131, 32))
        self.call_procedure_btn.setObjectName("call_procedure_btn")
        self.call_procedure_btn.clicked.connect(self.get_procedure_result)

        # Open in browser checkbox
        self.open_in_browser_label = QLabel(self.main)
        self.open_in_browser_label.setGeometry(QRect(240, 150, 131, 16))
        self.open_in_browser_label.setObjectName("open_in_browser_label")

        self.open_browser_checkbox = QCheckBox(self.main)
        self.open_browser_checkbox.setGeometry(QRect(240, 160, 40, 40))
        self.open_browser_checkbox.setObjectName("open_in_browser_checbox")
        self.open_browser_checkbox.stateChanged.connect(lambda: self.set_in_browser_checkbox(self.open_browser_checkbox))

        # Procedure parameter input
        self.procedure_param = QLineEdit(self.main)
        self.procedure_param.textChanged[str].connect(self.procedure_param_changed)
        self.procedure_param.setGeometry(QRect(240, 50, 131, 21))
        self.procedure_param.setInputMethodHints(Qt.ImhNone)
        self.procedure_param.setObjectName("procedure_param")

        # Document name text
        self.document_name_text = QLabel(self.main)
        self.document_name_text.setGeometry(QRect(420, 690, 131, 16))
        self.document_name_text.setObjectName("docuement_name_text")

        # Document name
        self.document_name = QLineEdit(self.main)
        self.document_name.textChanged[str].connect(self.document_name_changed)
        self.document_name.setGeometry(QRect(420, 710, 230, 21))
        self.document_name.setInputMethodHints(Qt.ImhNone)
        self.document_name.setObjectName("procedure_param")


        self.procedure_result = QTableWidget(self.main)
        self.procedure_result.setGeometry(QRect(420, 50, 1400, 600))
        self.procedure_result.setObjectName("procedure_result")



        self.get_document_btn = QPushButton(self.main)
        self.get_document_btn.setGeometry(QRect(660, 705, 213, 32))
        self.get_document_btn.setObjectName("get_document_btn")
        self.get_document_btn.clicked.connect(self.get_document_clicked)

        QMetaObject.connectSlotsByName(self.main)

        self.header_text.setText('Procedures')
        self.call_procedure_btn.setText("Call procedure")
        self.header_text_procedure_param.setText("Procedure parameter")
        self.header_text_procedure_param_2.setText("Procedure result")
        self.document_name_text.setText("Document name")
        self.get_document_btn.setText("Create document")
        self.header_text_documents.setText("Documents")
        self.open_in_browser_label.setText('Open in browser')

    def set_in_browser_checkbox(self, checkox):
        if checkox.isChecked():
            self.parent.check_open_in_browser(True)
        else:
            self.parent.check_open_in_browser(False)

    def set_table_data(self, columns, data):
        self.procedure_result.setRowCount(0)

        self.data = data

        row_count = len(data)
        column_count = len(columns)

        self.procedure_result.setRowCount(row_count)
        self.procedure_result.setColumnCount(column_count)

        self.procedure_result.setHorizontalHeaderLabels(columns)
        for i in range(len(columns)):
            self.procedure_result.setColumnWidth(i, len(columns[i]) + 150)

        for row in range(row_count):
            for column in range(column_count):
                item = list(data[row].values())[column]
                self.procedure_result.setItem(row, column, QTableWidgetItem(item))


    def document_clicked(self, item):
        self.parent.open_document(item.text())

    def document_name_changed(self, text):
        self.parent.set_document_name(text)

    def get_document_clicked(self):
        self.parent.get_document()

    def procedure_clicked(self, item):
        self.current_procedure = {
            'name': item.text()
        }
        self.document_name.setText(item.text())

    def procedure_param_changed(self, text):
        self.current_procedure['param'] = text


    def get_procedure_result(self):
        self.parent.call_procedure(self.current_procedure)

    def widget(self):
        return self.main

    def fill_procedure_list(self, names: list):
        excluded = self.parent.get_excluded_procedures()
        for name in names:
            if name not in excluded:
                self.procedures_list.addItem(name)

    def sync_document_list(self):
        self.documents_list.clear()
        files = self.parent.get_local_documents()
        for file in files:
            self.documents_list.addItem(file)

