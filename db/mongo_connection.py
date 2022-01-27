from pymongo import MongoClient
from loguru import logger
from os import getenv
from urllib.parse import quote_plus
from datetime import datetime

user = getenv("MONGO_USERNAME_PRIMARY")
password = getenv("MONGO_PASSWORD_PRIMARY")
host = str(getenv("MONGO_HOST_PRIMARY"))
db = getenv("MONGO_DATABASE_PRIMARY")
coll_sec = getenv("MONGO_COLLECTION_SEC")  # db to push results
MONGO_URL = "mongodb://%s:%s@%s" % (quote_plus(user), quote_plus(password), host)


# connect to db
def get_mongo_client():
    try:
        mongo_client = MongoClient(MONGO_URL)
        mongo_client.admin.authenticate(user, password)
        database = mongo_client[db]
        result_collection = database[coll_sec]
        return result_collection
    except Exception as e:
        logger.debug(f'Error while Connecting to Mongo Client: | Error:{e}')
        raise e
