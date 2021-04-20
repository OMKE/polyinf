

class User:

    ADMIN = 'admin'
    USER = 'user'

    def __init__(self, username: str, name: str, role: str):
        self.username = username
        self.name = name
        self.__set_role(role)

    def __set_role(self, role):
        if role != User.ADMIN or role != User.USER:
            raise ValueError('Role must be either `admin` or `user`')
        self.role = role
