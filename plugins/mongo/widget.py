from .core.database import Database
from .ui.ui_main_widget import MainWidgetUI
class MainWidget:

    def __init__(self, app):
        self.app = app
        self._database = Database()
        self._ui = MainWidgetUI(self, self.app.get_central_widget())


    def widget(self):
        return self._ui.widget()


    def get_procedures(self):
        cursor = self._database.cursor()
        cursor.execute("show procedure status where db=%s", (self._database.name(),))
        procedures = cursor.fetchall()
        procedure_names = [procedure[1] for procedure in procedures]
        return procedure_names



