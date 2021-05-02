from .core.database import Database
from .core.mongo import Mongo
from .ui.ui_main_widget import MainWidgetUI
from datetime import datetime
from core.support.config.config_provider import ConfigProvider
import os
from pkg_resources import resource_filename, resource_stream
import jinja2
import tempfile
from weasyprint import HTML

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWebEngineWidgets
import webbrowser

class MainWidget:

    def __init__(self, plugin, app):
        self.plugin = plugin
        self.app = app
        self._database = Database()
        self._mongo = Mongo()
        self._ui = MainWidgetUI(self, self.app.get_central_widget())
        self.document_name = ''
        self.data = None
        self.table_columns = []
        self.last_file = None
        self.html_view = QtWebEngineWidgets.QWebEngineView()
        self.open_in_browser = False


    def widget(self):
        return self._ui.widget()


    def get_procedures(self):
        cursor = self._database.cursor()
        cursor.execute("show procedure status where db=%s", (self._database.name(),))
        procedures = cursor.fetchall()
        procedure_names = [procedure[1] for procedure in procedures]
        return procedure_names

    def call_procedure(self, procedure):
        if self.validate_procedure(procedure):
            self.procedure = procedure
            cursor = self._database.cursor(dictionary=True)
            cursor.execute(f'USE {self._database.name()}')
            try:
                cursor.callproc(procedure['name'], (procedure['param'],))
                for result in list(cursor.stored_results()):
                    self.get_procedure_result(result.fetchall())
            except Exception as e:
                self.app.log(str(e), 'MongoPluginLogger')

    def set_document_name(self, name):
        self.document_name = name

    def check_open_in_browser(self, value):
        self.open_in_browser = value

    def get_document(self):
        if self.data is not None:
            name = self.document_name if self.document_name != '' else self.procedure['name']
            document_data = self.save_document_data()
            document = self._mongo.get_one(self.procedure['name'], document_data.inserted_id)
            now = datetime.now()
            created_at_file = now.strftime('%Y-%m-%d-%H-%M-%S')
            created_at = now.strftime('%d-%m-%Y - %H:%M-%S')
            data = {
                'name': name,
                'table_columns': self.table_columns,
                'data': document['data'],
                'created_at': created_at
            }
            template = self.get_template_file('pdf-template-1.html.jinja2')
            template_output = template.render(data=data)
            name = f'{name}-{created_at_file}'
            path = f'{self.get_document_path()}{os.sep}{name}.html'
            self.save_document_as_html(template_output, path)
            self.show_html_doc()
            self._ui.sync_document_list()
        else:
            self.app.log('No data found', 'MongoPluginLogger')


    def show_html_doc(self):
        if self.open_in_browser:
            webbrowser.open_new_tab(f'file://{self.last_file}')
        else:
            self.html_view.load(QUrl().fromLocalFile(self.last_file))
            self.html_view.showMaximized()

    def get_local_documents(self):
        path = self.get_document_path()
        files = os.listdir(path)
        return [file for file in files if ".html" in file]

    def open_document(self, file_name):
        path = f'{self.get_document_path()}{os.sep}{file_name}'
        if self.open_in_browser:
            webbrowser.open_new_tab(f'file://{path}')
        else:
            self.html_view.load(QUrl().fromLocalFile(path))
            self.html_view.showMaximized()

    def save_document_as_html(self, template_output, path):
        self.last_file = path
        with open(path, 'w') as file:
            file.write(template_output)


    def get_templates_path(self):
        return f'{self.plugin.icon()[0:-8]}templates{os.sep}'

    def get_template_file(self, file_name):
        path = f'{self.get_templates_path()}{file_name}'
        file = open(path)
        file_content = file.read()
        file.close()
        return jinja2.Template(file_content, trim_blocks=True)

    def get_document_path(self):
        path = f'{ConfigProvider().logs_path()}{os.sep}documents'
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def get_excluded_procedures(self):
        return ConfigProvider().get_config('excludedDirectives')


    def save_document_data(self):
        name = self.procedure['name']
        collection = self._mongo.create_collection(name)
        try:
            return self._mongo.insert(name, self.data)
        except Exception as e:
            return self._mongo.get_all(name)

    def get_procedure_result(self, data):
        self.data = {}
        if len(data) > 0:
            self.data = data
            self.table_columns = list(data[0].keys())
            self._ui.set_table_data(self.table_columns, data)

    def validate_procedure(self, procedure):
        parameters = []
        if not "name" in procedure:
            parameters.append('Procedure not selected')
        if not "param" in procedure:
            parameters.append('Procedure parameter is blank')

        if len(parameters) == 0:
            return True
        self.app.log(f'{", ".join(parameters)}')
        return False
