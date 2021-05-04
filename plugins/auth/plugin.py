from core.models.user import User
from core.plugin.plugin import Plugin
from core.plugin.plugin_guards import PluginGuards
from .ui.auth_widget import AuthWidget
from .utils.auth_interface_concrete import AuthInterfaceConcrete

class Main(Plugin):
    def __init__(self, app, plugin_specification):
        super().__init__(app, plugin_specification)
        self._ui = AuthWidget(self)

    def activate(self):
        self.app.log(f'{self.name()} activated')

    def deactivate(self):
        self.app.log(f'{self.name()} deactivated')

    def login_user(self, user):
        if user is not None and len(user) > 0:
            data = User(user[3], f'{user[1]} {user[2]}', user[-1])
            auth_interface_imp = AuthInterfaceConcrete(data)
            self.app.get('managers', 'AuthManager').login(auth_interface_imp)
            self.app.log('Successful login')
        else:
            self.app.log('Wrong credentials')

    def register_user(self, user):
        if user:
            self.app.log('Successful registration. You can log in now')
        else:
            self.app.log('Unsuccesful registration. Try again')

    def widget(self, parent=None):
        return self._ui.widget()

    def guard(self) -> str:
        return PluginGuards.NONE
