from dataclasses import asdict
from datetime import datetime

import pymongo

from reading import Reading

class Mongo:
    def __init__(self):
        self.client = pymongo.MongoClient(
            "mongodb+srv://oryx-server:password2219@impala.ine2k.mongodb.net/readings?retryWrites=true&w=majority")
        self.db = self.client.impala
        self.collection = self.db.readings

    def insert(self, reading: Reading):
        self.collection.insert_one(reading.to_dict())
