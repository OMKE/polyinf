from core.support.log.logger import Logger
from core.support.config.config_provider import ConfigProvider

class MongoPluginLogger(Logger):

    def __init__(self):
        super().__init__(f'{ConfigProvider().logs_path()}/mongo-plugin-log.txt')

    def log(self, message: str):
        with open(self.path, 'a') as log_file:
            log_file.write(f'{self.timestamp()} - {message} \n')

        if self.status_bar:
            self.status_bar.showMessage(message, 3000)