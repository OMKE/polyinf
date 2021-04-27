from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from plugins.auth.utils.db_utils import connection, use_database, get_all_columns, register_user

class RegistrationForm(QDialog):
    def __init__(self):
        super().__init__()
        self.current_connection = None
        self.current_cursor = None
        connection("localhost", "root", "root", self)
        use_database("polyinf_db", self)
        self.columns_sorted = get_all_columns(self)
        self.initiate_view()

    def initiate_view(self):
        for i in self.columns_sorted:
            setattr(self, i["name"], QLineEdit(self))
            getattr(self, i["name"]).setGeometry(QRect(800, i["cordinates"], 201, 21))
            getattr(self, i["name"]).setPlaceholderText(i["display_name"])

        self.reg_button = QPushButton('Register', self)
        self.reg_button.setGeometry(QRect(800, 440, 201, 21))

        self.login_button = QPushButton('Login', self)
        self.login_button.setGeometry(QRect(800, 480, 201, 21))

        self.reg_button.clicked.connect(self.register_event)
        self.login_button.clicked.connect(self.login_event)

        self.show()

    @pyqtSlot()
    def register_event(self):
        first_name_value = self.first_name.text()
        last_name_value = self.last_name.text()
        email_value = self.email.text()
        password_value = self.password.text()
        if len(first_name_value) > 0 and len(last_name_value) > 0 and len(email_value) > 0 and len(password_value) > 0:
            register_user(self, first_name_value, last_name_value, email_value, password_value)
        

    @pyqtSlot()
    def login_event(self):
        print("TRIGGERED")