import mysql.connector
from core.support.config.config_provider import ConfigProvider
from .connector import Connector

class Database(Connector):

    def __init__(self):
        super().__init__()
        self.connection = self.connect()

    def connection(self):
        return self.connection()

    def cursor(self, dictionary=False):
        if dictionary:
            return self.connection.cursor(dictionary=True)
        return self.connection.cursor()


    def connect(self):
        config = ConfigProvider().mysql()
        return mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            database=config['database'],
            buffered=True
        )


    def name(self):
        config = ConfigProvider().mysql()
        return config['database']