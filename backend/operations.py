""" News Operations """
import json
import os
import pickle
import redis
import sys

from datetime import datetime
from bson.json_util import dumps

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client # pylint: disable=import-error


NEWS_TABLE_NAME = 'news'
NEWS_LIST_SIZE = 10
NEWS_LIMIT = 200

USER_NEWS_TIME_OUT_IN_SECONDS = 3600

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT, db=0)


def get_one_news():
    """ Get one news from mongoDB """
    database = mongodb_client.get_db()
    news = database[NEWS_TABLE_NAME].find_one()
    return news


def get_news_summaries_for_user(user_id, page_num):
    page_num = int(page_num)
    begin_index = (page_num - 1) * NEWS_LIST_SIZE
    end_index = page_num * NEWS_LIST_SIZE

    sliced_news = []

    if redis_client.get(user_id) is not None:
        news_digests = pickle.loads(redis_client.get(user_id))
        sliced_news_digests = news_digests[begin_index: end_index]
        print sliced_news_digests
        db = mongodb_client.get_db()
        sliced_news = list(db[NEWS_TABLE_NAME].find({'digest': {'$in': sliced_news_digests}}))
    else:
        db = mongodb_client.get_db()
        total_news = list(db[NEWS_TABLE_NAME].find().sort([('publishedAt', -1)]).limit(NEWS_LIMIT))
        total_news_digests = map(lambda x:x['digest'], total_news)
        redis_client.set(user_id, pickle.dumps(total_news_digests))
        redis_client.expire(user_id, USER_NEWS_TIME_OUT_IN_SECONDS)

        sliced_news = total_news[begin_index: end_index]


    for news in sliced_news:
        # Remove text from news
        del news['text']
        if news['publishedAt'].date() == datetime.today().date():
            news['time'] = 'today'

    return json.loads(dumps(sliced_news))