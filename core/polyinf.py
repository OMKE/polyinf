from .foundation.managers.plugin_manager import PluginManager
from .foundation.managers.auth_manager import AuthManager
from .support.foundation.manager import Manager
from app.application import Application
from core.util.loggers.simple_logger import SimpleLogger
from typing import List


class PolyInf:

    def __init__(self, args):
        self.app = Application(args)
        self.start()

    def __managers(self) -> List[Manager]:
        return [
            PluginManager(self.app),
            AuthManager(self.app),
        ]

    def start(self) -> int:
        self.__boot_managers()
        self.__bind()
        self.app.start()

    def __boot_managers(self) -> None:
        for manager in self.__managers():
            manager.call_booting_callbacks()
            manager.boot()
            manager.call_booted_callbacks()
            self.app.bind('managers', manager)

    def __bind(self) -> None:
        self.app.bind('loggers', SimpleLogger())
