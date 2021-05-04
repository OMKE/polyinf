from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from ....main.utils.db_utils import connection, use_database, get_all_tables, get_table_data
from core.support.config.config_provider import ConfigProvider


class GetDataWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.current_connection = None
        self.current_cursor = None

        self.tables = None
        self.data = None

        self.config = mysql_info = ConfigProvider().mysql()
        connection(
            mysql_info["host"], mysql_info["user"], mysql_info["password"], self)
        use_database(mysql_info["database"], self)

        self.getTables()
        self.initUI()

    def getTables(self):
        self.current_cursor.execute("SHOW TABLES")
        tables = self.current_cursor.fetchall()
        tables = [''.join(i) for i in tables]
        self.tables = tables

    def initUI(self):
        self.setObjectName("Form")
        self.resize(1200, 900)
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QRect(30, 20, 141, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(self.tables)
        self.getDataBtn = QPushButton(self)
        self.getDataBtn.setGeometry(QRect(50, 90, 111, 41))
        self.getDataBtn.setObjectName("getDataBtn")
        self.getDataBtn.clicked.connect(self.getTableData)

        self.retranslateUi(self)
        self.show()

    def initTableUI(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(QRect(200, 150, 900, 700))
        self.tableWidget.setRowCount(len(self.data[1]))
        self.tableWidget.setColumnCount(len(self.data[0]))
        self.tableWidget.setObjectName("Table data")
        self.tableWidget.setHorizontalHeaderLabels(x for x in self.data[0])

        row = 0


        for x in self.data[1]:
            for index, y in enumerate(x):
                item = QTableWidgetItem()
                item.setText(str(y))
                self.tableWidget.setItem(row, index, item)
            row += 1

        self.tableWidget.show()

    @pyqtSlot()
    def getTableData(self):
        table_name = str(self.comboBox.currentText())
        data = get_table_data(self, table_name)
        self.data = [x for x in data]
        self.initTableUI()

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate(
            "Form", "Forma za dobavljanje podataka"))
        self.getDataBtn.setText(_translate("Form", "Dobavi podatke"))
