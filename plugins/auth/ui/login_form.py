from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from plugins.auth.utils.db_utils import connection, use_database, get_all_columns, register_user, login_user
from core.support.config.config_provider import ConfigProvider

class LoginForm(QDialog):
    def __init__(self, view):
        super().__init__()
        self.change_view = view
        self.current_connection = None
        self.current_cursor = None
        mysql_info = ConfigProvider().mysql()
        connection(mysql_info["host"], mysql_info["user"], mysql_info["password"], self)
        use_database(mysql_info["database"], self)
        self.initiate_view()
    
    def initiate_view(self):
        self.email = QLineEdit(self)
        self.email.setGeometry(QRect(800, 280, 201, 21))
        self.email.setPlaceholderText("Email")

        self.password = QLineEdit(self)
        self.password.setGeometry(QRect(800, 320, 201, 21))
        self.password.setPlaceholderText("Password")

        self.reg_button = QPushButton('Register', self)
        self.reg_button.setGeometry(QRect(800, 360, 201, 21))

        self.login_button = QPushButton('Login', self)
        self.login_button.setGeometry(QRect(800, 400, 201, 21))

        self.reg_button.clicked.connect(self.register_event)
        self.login_button.clicked.connect(self.login_event)

        self.label = QLabel('', self)
        self.label.setGeometry(QRect(850, 450, 201, 21))

        self.show()


    @pyqtSlot()
    def register_event(self):
        self.change_view()

    @pyqtSlot()
    def login_event(self):
        email_value = self.email.text()
        password_value = self.password.text()
        if len(email_value) > 0 and len(password_value) > 0:
            logged_user = login_user(self, email_value, password_value)
            
            if logged_user:
                label_value = self.label.setText('Successful login!')
            else:
                label_value = self.label.setText('Unsuccessful login!')

            return logged_user