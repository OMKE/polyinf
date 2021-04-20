from abc import abstractmethod
from datetime import datetime
from .logger_interface import LoggerInterface
from core.support.config.config_provider import ConfigProvider
from PyQt5.QtWidgets import QStatusBar


class Logger(LoggerInterface):

    def __init__(self, path):
        self.path = path
        self.status_bar = None

    def attach(self, status_bar: QStatusBar):
        self.status_bar = status_bar

    def timestamp(self):
        now = datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')
