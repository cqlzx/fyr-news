""" News Operations """
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client # pylint: disable=import-error

NEWS_TABLE_NAME = 'news'


def get_one_news():
    """ Get one news from mongoDB """
    database = mongodb_client.get_db()
    news = database[NEWS_TABLE_NAME].find_one()
    return news
