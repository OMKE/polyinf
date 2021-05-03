import sys

from core.support.foundation.manager import Manager
from core.plugin.auth_interface import AuthInterface
from core.models.user import User


class AuthManager(Manager):

    def __init__(self, app):
        super().__init__(app)
        self._loggedIn = False
        self._user = None

    def boot(self):
        pass

    def logged_in(self) -> bool:
        return self._loggedIn

    def user(self):
        return self._user

    def login(self, auth_interface: AuthInterface):
        self._loggedIn = True
        self._user = auth_interface.user()
        self.app.log(f'User: {self._user.name} logged in.')
        self.app.refresh()
        self.redirect(login=True)

    def redirect(self, login=True):
        for plugin in self.app.get('managers', 'PluginManager').get_all():
            if login:
                if plugin.name() == "MainPlugin":
                    self.app.set_central_widget(plugin.widget())
            else:
                sys.exit()



    # Method only for development purposes
    def force_login(self, role='user'):
        self._loggedIn = True
        self._user = User("dev@polyinf.com", 'dev', role)

    def logout(self):
        self.app.log(f'User: {self._user.name} logged out.')
        self._loggedIn = False
        self._user = None
        self.redirect(login=False)

