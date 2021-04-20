

class ContainerEntityNotFoundException(Exception):
    def __init__(self, message="Container entity could not be found"):
        super().__init__(message)


class ContainerKeyNotFound(Exception):
    def __init__(self, message="Container key could not be found"):
        super().__init__(message)


class ConfigFileNotFoundException(Exception):
    def __init__(self, message="Config file could not be found"):
        super().__init__(message)


class PluginNotFound(Exception):
    def __init__(self, message="Plugin with provided name could not be found"):
        super().__init__(message)
