from pymongo import MongoClient
from .connector import Connector
from core.support.config.config_provider import ConfigProvider
from datetime import datetime

class Mongo(Connector):

    def __init__(self):
        super().__init__()
        config = ConfigProvider().mongo()
        self.client = MongoClient(f'mongodb://{config["host"]}:{config["port"]}/')
        self.database = self.client[config['database']]


    def connection(self):
        return self.database

    # def databases(self):
    #     return self.client.list_database_names()

    def collections(self):
        return self.database.list_collection_names()

    def create_collection(self, name):
        try:
            return self.database.create_collection(name)
        except Exception as e:
            return self.collection(name)

    def collection(self, name):
        return self.database[name]

    def get_all(self, collection_name):
        collection = self.collection(collection_name)
        return [column for column in collection.find()]

    def get_one(self, collection_name, id):
        collection = self.collection(collection_name)
        return collection.find_one({"_id": id})

    def insert(self, collection_name, data):
        collection = self.collection(collection_name)
        document_name = f'{collection_name}-{self.time_stamp()}'
        document = {
            'name': document_name,
            'data': data
        }
        return collection.insert_one(document)


    def time_stamp(self) -> str:
        now = datetime.now()
        return now.strftime('%Y-%m-%d-%H-%M-%S')