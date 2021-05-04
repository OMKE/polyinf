from core.models.user import User
from core.plugin.auth_interface import AuthInterface


class AuthInterfaceConcrete(AuthInterface):

    def __init__(self, user: User):
        self._user = user

    def user(self) -> User:
        return self._user
