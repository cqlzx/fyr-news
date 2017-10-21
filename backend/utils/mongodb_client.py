""" MongoDB client """

from pymongo import MongoClient

MONGO_DB_HOST = 'localhost'
MONGO_DB_PORT = 27017
DB_NAME = 'fyr-news'

CLIENT = MongoClient("%s:%s" % (MONGO_DB_HOST, str(MONGO_DB_PORT)))


def get_db(database=DB_NAME):
    """ get database """
    database = CLIENT[database]
    return database
