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

    def environment(self) -> str:
        return self.get_config('env')

    def development(self) -> bool:
        return self.environment() == 'DEV'

    def production(self) -> bool:
        return self.environment() == 'PROD'

    def name(self) -> str:
        return self.config['name']

    def plugins_path(self) -> str:
        return self.config['pluginsPath']

    def logs_path(self) -> str:
        path = self.path(self.config['logsPath'])
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def mysql_log_path(self) -> str:
        return f'{self.logs_path()}/mysql-log.txt'

    def mongo_log_path(self) -> str:
        return f'{self.logs_path()}/mongo-log.txt'

    def arango_log_path(self) -> str:
        return f'{self.logs_path()}/arango-log.txt'

    def env_config(self) -> str:
        return self.config['env']

    def get_config(self, connection_key):
        with open(self.env_config(), 'r') as file:
            return load(file)[connection_key]

    def app_key(self):
        return self.get_config('key')

    def mysql(self):
        return self.get_config('mysql')

    def mongo(self):
        return self.get_config('mongo')