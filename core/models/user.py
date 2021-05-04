
class User:

    ADMIN = 'admin'
    USER = 'user'

    def __init__(self, email: str, name: str, role: str):
        self.email = email
        self.name = name
        self.__set_role(role)

    def __set_role(self, role):
        if role != User.ADMIN and role != User.USER:
            raise ValueError('Role must be either `admin` or `user`')
        self.role = role

    def get_role(self):
        return self.role
