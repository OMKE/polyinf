from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from plugins.admin.utils.db_utils import get_users, connection, use_database, promote_user
from core.support.config.config_provider import ConfigProvider

class AdminDashboard:
    def __init__(self, parent):
        self.current_connection = None
        self.current_cursor = None
        self.setup()
        self.users = get_users(self)

        self.parent = parent
        self.main = QWidget()
        self.main.setObjectName("Admin Widget")
        self.main.resize(1536, 966)
        self.initiate_view()

    def initiate_view(self):
        self.tableWidget = QtWidgets.QTableWidget(self.main)
        self.tableWidget.setGeometry(QtCore.QRect(160, 85, 600, 600))
        labels = ["ID","First Name","Last Name", "Email", "Password", "Role"]
        self.tableWidget.setRowCount(len(self.users))
        self.tableWidget.setColumnCount(len(labels))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(labels)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        for i in range(len(self.users)):
            user = self.users[i]
            if user[-1] != 'admin':
                button = QPushButton(self.main)
                button.setGeometry(QRect(760, 110 + (i * 30), 100, 30))
                button.setText('Make admin')
                button.clicked.connect(lambda state, id=user[0], btn=button: self.make_admin(btn, id))
            for j in range(len(user)):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(user[j])))


    def make_admin(self, button: QPushButton, user_id):
        promote_user(self, tuple(str(user_id)))
        self.tableWidget.deleteLater()
        self.users = get_users(self)
        self.initiate_view()
        self.tableWidget.show()
        button.deleteLater()

    def setup(self):
        mysql_info = ConfigProvider().mysql()
        connection(mysql_info["host"], mysql_info["user"], mysql_info["password"], self)
        use_database(mysql_info["database"], self)

    def widget(self):
        return self.main

