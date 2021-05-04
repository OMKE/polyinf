from abc import ABC


class Connector(ABC):
    def __init__(self):
        super(Connector, self).__init__()

    def connection(self):
        raise NotImplementedError('Must be implemeted by a subclass')
