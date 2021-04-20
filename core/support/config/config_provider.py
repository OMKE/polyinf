import sys
from json import load
import os
from core.exceptions.exc import ConfigFileNotFoundException


class ConfigProvider:

    def __init__(self):
        self.configPath = os.path.join(sys.path[0], 'config.json')
        self.config = self.open()

    def open(self) -> None:
        try:
            with open(self.configPath, 'r') as config_file:
                return load(config_file)
        except IOError:
            raise ConfigFileNotFoundException()

    def path(self, file_name) -> str:
        return os.path.join(sys.path[0], file_name)

    def name(self) -> str:
        return self.config['name']

    def plugins_path(self) -> str:
        return self.config['pluginsPath']

    def logs_path(self) -> str:
        return self.path(self.config['logsPath'])

    def mysql_log_path(self) -> str:
        return f'{self.logs_path()}/mysql-log.txt'

    def mongo_log_path(self) -> str:
        return f'{self.logs_path()}/mongo-log.txt'

    def arango_log_path(self) -> str:
        return f'{self.logs_path()}/arango-log.txt'

    def database_config_path(self) -> str:
        return self.config['databaseConfigPath']
