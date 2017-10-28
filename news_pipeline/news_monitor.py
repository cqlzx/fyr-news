import datetime
import hashlib
import os
import redis
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import news_api_client
from cloud_amqp_client import CloudAmqpClient

REDIS_CLIENT = 'localhost'
REDIS_PORT = 6379

SLEEP_TIME_IN_SECONDS = 10
TIME_OUT_IN_SECONDS = 24 * 60 * 60

FYR_NEWS_QUEUE_URL = 'amqp://mlcafzrx:i3YEi-GptkW4ntHLh0mTV_zzc9qs4hGU@donkey.rmq.cloudamqp.com/mlcafzrx'
SCRAPE_TASK_QUEUE = 'fyr-news-scrape-task'

NEWS_SOURCE = [
    'bbc-news',
    'bbc-sport',
    'bloomberg',
    'cnn',
    'entertainment-weekly',
    'espn',
    'ign',
    'techcrunch',
    'the-new-york-times',
    'the-wall-street-journal',
    'the-washington-post'
]

redis_client = redis.StrictRedis(REDIS_CLIENT, REDIS_PORT)
cloudAmqpClient = CloudAmqpClient(FYR_NEWS_QUEUE_URL, SCRAPE_TASK_QUEUE)

while True:
    news_list = news_api_client.get_news_by_sources(NEWS_SOURCE)

    num_of_new_news = 0

    for news in news_list:
        news_digest = hashlib.md5(news['title'].encode('utf-8')).digest().encode('base64')
        if redis_client.get(news_digest) is None:
            num_of_new_news += 1
            news['digest'] = news_digest

            if news['publishedAt'] is None:
                news['publishedAt'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

            redis_client.set(news_digest, news)
            redis_client.expire(news_digest, TIME_OUT_IN_SECONDS)

            cloudAmqpClient.send_message(news)

    print 'News monitor fetched %d news' % num_of_new_news

    cloudAmqpClient.sleep(SLEEP_TIME_IN_SECONDS)