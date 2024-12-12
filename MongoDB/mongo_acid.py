from pymongo import MongoClient, WriteConcern, ReadPreference
from pymongo.errors import PyMongoError
from pymongo.synchronous.client_session import ClientSession

import os
import dotenv
from pathlib import Path


dotenv.load_dotenv(Path('.env'))  # {...}
client = MongoClient(os.environ.get('MONGO_URI'))


db = client.get_database(
    name=os.environ.get('TARGET_DB'),
    write_concern=WriteConcern(w="majority")
) # use db

collection = db.get_collection(
    name=os.environ.get('TARGET_COLLECTION'),
    write_concern=WriteConcern(w="majority"),
    read_preference=ReadPreference.PRIMARY
)


session: ClientSession = client.start_session()


with session.start_transaction():
    try:
        collection.update_one(
            {"name": "Alice"},
            {"$inc": {"balance": -90}},
            session=session
        )

        alice = collection.find_one(
            {"name": "Alice"},
            session=session
        )

        if alice['balance'] < 0:
            raise ValueError("Balance cannot be negative")

        collection.update_one(
            {"name": "Bob"},
            {"$inc": {"balance": 90}},
            session=session
        )

    except (PyMongoError, ValueError) as e:
        print(f"ERROR, transaction will be aborted: [{e}]")
        session.abort_transaction()
    else:
        session.commit_transaction()
    finally:
        session.end_session()
        client.close()
