from pymongo import MongoClient, WriteConcern, ReadPreference
import os
import dotenv
from pathlib import Path


class MongoDBMFinder:
    def __init__(self, batch_size):
        self.collection = self.get_db_connect()
        self.last_id = None
        self.batch_size = batch_size

    def get_db_connect(self):
        dotenv.load_dotenv(Path('../.env'))
        client = MongoClient(
            os.environ.get('MONGO_URI'),
            tls=True,
            tlsAllowInvalidCertificates=True
        )

        db = client.get_database(
            name=os.environ.get('TARGET_DB'),
            write_concern=WriteConcern(w="majority")
        )

        collection = db.get_collection(
            name=os.environ.get('TARGET_COLLECTION'),
            write_concern=WriteConcern(w="majority"),
            read_preference=ReadPreference.PRIMARY
        )
        return collection

    def find_all(self):
        if self.last_id is None:
            query = {}
        else:
            query = {"_id": {"$gt": self.last_id}, "plot": {"$exists": True}}

        cursor = self.collection.find(query, {"plot": 1, "_id": 1}) \
            .sort("_id", 1) \
            .limit(self.batch_size)

        docs = list(cursor)
        self.last_id = docs[-1]["_id"]
        return [doc.get('plot') for doc in docs if 'plot' in doc]





