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
import news_recommendation_service_client

from cloud_amqp_client import CloudAmqpClient

NEWS_TABLE_NAME = 'test-news'
LOG_CLICK_TABLE_NAME = 'click_logs'
NEWS_LIST_SIZE = 10
NEWS_LIMIT = 200

USER_NEWS_TIME_OUT_IN_SECONDS = 3600

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

FYR_NEWS_QUEUE_URL = 'amqp://mlcafzrx:i3YEi-GptkW4ntHLh0mTV_zzc9qs4hGU@donkey.rmq.cloudamqp.com/mlcafzrx'
LOG_CLICK_QUEUE = 'fyr-news-log-click-task'

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT, db=0)
cloudAMQP_client = CloudAmqpClient(FYR_NEWS_QUEUE_URL, LOG_CLICK_QUEUE)

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

    # Get preference for user
    preference = news_recommendation_service_client.getPreferenceForUser(user_id)
    topPreference = None

    if preference is not None and len(preference) > 0:
        topPreference = preference[0]

    for news in sliced_news:
        # Remove text from news
        del news['text']
        if news['class'] == topPreference:
            news['reason'] = 'Recommend'
        if news['publishedAt'].date() == datetime.today().date():
            news['time'] = 'today'

    return json.loads(dumps(sliced_news))


def log_news_click_for_user(user_id, news_id):
    message = {'userId': user_id, 'newsId': news_id, 'timestamp': datetime.utcnow()}

    db = mongodb_client.get_db()
    db[LOG_CLICK_TABLE_NAME].insert(message)

    # Send log task to machine learning service for prediction
    message = {'userId': user_id, 'newsId': news_id, 'timestamp': str(datetime.utcnow())}
    cloudAMQP_client.send_message(message)