from core.support.log.logger import Logger
from core.support.config.config_provider import ConfigProvider


class SimpleLogger(Logger):

    def __init__(self):
        super().__init__(f'{ConfigProvider().logs_path()}/log.txt')

    def log(self, message: str):
        with open(self.path, 'a') as log_file:
            log_file.write(f'{self.timestamp()} - {message} \n')

        self.status_bar.showMessage(message, 3000)
