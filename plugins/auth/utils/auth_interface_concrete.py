from core.models.user import User
from core.plugin.auth_interface import AuthInterface
from plugins.auth.utils.db_utils import login_user

class AuthInterfaceConcrete(AuthInterface):

    def __init__(self, user: User):
        self._user = user

    def user(self) -> User:
        return self._user
