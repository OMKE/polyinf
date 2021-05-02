from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from core.support.config.config_provider import ConfigProvider
from plugins.auth.utils.db_utils import connection, use_database, get_all_columns, register_user, login_user

class AuthWidget:

    def __init__(self, parent):
        self.parent = parent
        self.setup()
        self.main = QWidget()
        self.main.setObjectName("Auth Widget")
        self.main.resize(936, 766)

        self.tabWidget = QTabWidget(self.main)
        self.tabWidget.setGeometry(QRect(500, 200, 800, 600))
        self.tabWidget.setObjectName("tabWidget")
        self.login = QWidget()
        self.login.setAccessibleName("")
        self.login.setObjectName("login")
        self.email_input = QLineEdit(self.login)
        self.email_input.setGeometry(QRect(300, 140, 171, 21))
        self.email_input.setObjectName("email_input")
        self.email_label = QLabel(self.login)
        self.email_label.setGeometry(QRect(300, 120, 60, 16))
        self.email_label.setObjectName("email_label")
        self.password_input = QLineEdit(self.login)
        self.password_input.setGeometry(QRect(300, 200, 171, 21))
        self.password_input.setObjectName("password_input")
        self.password_label = QLabel(self.login)
        self.password_label.setGeometry(QRect(300, 180, 60, 16))
        self.password_label.setObjectName("password_label")

        self.login_btn = QPushButton(self.login)
        self.login_btn.setGeometry(QRect(325, 250, 113, 32))
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(self.login_event)


        self.tabWidget.addTab(self.login, "")
        self.register = QWidget()
        self.register.setObjectName("register")
        self.first_name_label = QLabel(self.register)
        self.first_name_label.setGeometry(QRect(300, 100, 71, 16))
        self.first_name_label.setObjectName("first_name_label")
        self.first_name_input = QLineEdit(self.register)
        self.first_name_input.setGeometry(QRect(300, 120, 161, 21))
        self.first_name_input.setObjectName("first_name_input")
        self.last_name_input = QLineEdit(self.register)
        self.last_name_input.setGeometry(QRect(300, 180, 161, 21))
        self.last_name_input.setObjectName("last_name_input")
        self.last_name_label = QLabel(self.register)
        self.last_name_label.setGeometry(QRect(300, 160, 71, 16))
        self.last_name_label.setObjectName("last_name_label")
        self.email_input_register = QLineEdit(self.register)
        self.email_input_register.setGeometry(QRect(300, 240, 161, 21))
        self.email_input_register.setObjectName("email_input_register")
        self.email_label_2 = QLabel(self.register)
        self.email_label_2.setGeometry(QRect(300, 220, 71, 16))
        self.email_label_2.setObjectName("email_label_2")
        self.password_label_register = QLabel(self.register)
        self.password_label_register.setGeometry(QRect(300, 270, 71, 16))
        self.password_label_register.setObjectName("password_label_register")
        self.password_input_register = QLineEdit(self.register)
        self.password_input_register.setGeometry(QRect(300, 290, 161, 21))
        self.password_input_register.setObjectName("password_input_register")

        self.register_btn = QPushButton(self.register)
        self.register_btn.setGeometry(QRect(320, 340, 113, 32))
        self.register_btn.setObjectName("register_btn")
        self.register_btn.clicked.connect(self.register_event)

        self.tabWidget.addTab(self.register, "")
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self.main)

        self.email_input.setPlaceholderText("johndoe@gmail.com")
        self.email_label.setText("Email")
        self.password_input.setPlaceholderText("*********")
        self.password_label.setText("Password")
        self.login_btn.setText("Login")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login), "Login")
        self.first_name_label.setText("First name")
        self.first_name_input.setPlaceholderText("John")
        self.last_name_input.setPlaceholderText("Doe")
        self.last_name_label.setText("Last name")
        self.email_input_register.setPlaceholderText("johndoe@gmail.com")
        self.email_label_2.setText("Email")
        self.password_label_register.setText("Password")
        self.password_input_register.setPlaceholderText("**********")
        self.register_btn.setText("Register")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.register), "Register")

    def login_event(self):
        email_value = self.email_input.text()
        password_value = self.password_input.text()
        if len(email_value) > 0 and len(password_value) > 0:
            logged_user = login_user(self, email_value, password_value)
            if len(logged_user) > 0:
                self.parent.login_user(logged_user[0])
            else:
                self.parent.login_user(None)
        else:
            self.parent.login_user(None)

    def register_event(self):
        first_name_value = self.first_name_input.text()
        last_name_value = self.last_name_input.text()
        email_value = self.email_input_register.text()
        password_value = self.password_input_register.text()
        if len(first_name_value) > 0 and len(last_name_value) > 0 and len(email_value) > 0 and len(password_value) > 0:
            registered_user = register_user(self, first_name_value, last_name_value, email_value, password_value)
            if registered_user:
                self.parent.register_user(registered_user)
        else:
            self.parent.register_user(None)

    def setup(self):
        mysql_info = ConfigProvider().mysql()
        self.current_connection = connection(mysql_info["host"], mysql_info["user"], mysql_info["password"], self)
        use_database(mysql_info["database"], self)


    def widget(self):
        return self.main

