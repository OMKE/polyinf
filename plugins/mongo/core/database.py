import mysql.connector
from core.support.config.config_provider import ConfigProvider

class Database:

    def __init__(self):
        self.connection = self.connect()

    def cursor(self):
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