from core.support.foundation.manager import Manager
from core.plugin.auth_interface import AuthInterface


class AuthManager(Manager):

    def __init__(self, app):
        super().__init__(app)
        self._loggedIn = False
        self._user = None

    def boot(self):
        pass

    def logged_in(self) -> bool:
        return self.loggedIn

    def user(self):
        return self._user

    def login(self, auth_interface: AuthInterface):
        self._loggedIn = True
        self._user = auth_interface.user()
        self.app.log(f'User: {self._user.name} logged in.')

    def logout(self):
        self.app.log(f'User: {self._user.name} logged out.')
        self._loggedIn = False
        self._user = None
