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
        self.tableWidget.setGeometry(QtCore.QRect(160, 85, 900, 600))
        self.tableWidget.setRowCount(len(self.users))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(["ID","First Name","Last Name", "Email", "Password", "Role", "Promote"])
        self.tableWidget.setEditTriggers( QtWidgets.QTableWidget.NoEditTriggers )

        tablerow=0

        for user in self.users:
            for index, value in enumerate(user):
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(value))
                self.tableWidget.setItem(tablerow, index, item)

            self.promote_btn = QtWidgets.QTableWidgetItem()
            role = user[-1]
            if role == 'user':
                self.promote_btn.setText("MAKE ADMIN")
                self.tableWidget.setItem(tablerow, 6, self.promote_btn)

            tablerow+=1

        self.tableWidget.clicked.connect(self.make_admin)

    def make_admin(self, item):
        if(item.column() == 6):
            user_id = self.users[item.row()][0]
            promote_user(self, tuple(str(user_id)))
            self.tableWidget.deleteLater()
            self.users = get_users(self)
            self.initiate_view()
            self.tableWidget.show()

    def setup(self):
        mysql_info = ConfigProvider().mysql()
        connection(mysql_info["host"], mysql_info["user"], mysql_info["password"], self)
        use_database(mysql_info["database"], self)

    def widget(self):
        return self.main

