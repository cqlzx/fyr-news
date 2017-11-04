import datetime
import sys
import os

from dateutil import parser
from sklearn.feature_extraction.text import TfidfVectorizer

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloud_amqp_client import CloudAmqpClient
import news_topic_modeling_service_client
import mongodb_client

DB_COLLECTION_NAME = 'test-news'

SLEEP_TIME_IN_SECONDS = 1

DUPLICATE_THRESHOLD = 0.9

FYR_NEWS_QUEUE_URL = 'amqp://mlcafzrx:i3YEi-GptkW4ntHLh0mTV_zzc9qs4hGU@donkey.rmq.cloudamqp.com/mlcafzrx'
DEDUPE_TASK_QUEUE = 'fyr-news-dedupe-task'

dedupe_queue_client = CloudAmqpClient(FYR_NEWS_QUEUE_URL, DEDUPE_TASK_QUEUE)


def handle_message(message):
    if message is None or not isinstance(message, dict):
        print 'Invalid message!'
        return
    task = message
    text = task['text']

    if text is None:
        return

    published_at = parser.parse(task['publishedAt'])
    published_start_time = datetime.datetime(published_at.year, published_at.month, published_at.day)
    published_end_time = published_start_time + datetime.timedelta(days = 1)

    db = mongodb_client.get_db()
    same_day_news_list = list(db[DB_COLLECTION_NAME].find({'publishedAt': {'$gte': published_start_time, '$lt': published_end_time}}))

    if same_day_news_list is not None and len(same_day_news_list) > 0:

        documents = [news['text'] for news in same_day_news_list]
        documents.insert(0, text)

        tfidf = TfidfVectorizer().fit_transform(documents)
        pairwise_sim = tfidf * tfidf.T

        print pairwise_sim

        rows, _ = pairwise_sim.shape

        for row in range(1, rows):
            if pairwise_sim[row, 0] > DUPLICATE_THRESHOLD:
                print 'Duplicate news!'

                return

    task['publishedAt'] = parser.parse(task['publishedAt'])

    title = task['title']
    if title is None:
        title = task['description']
    topic = news_topic_modeling_service_client.classify(title)
    task['class'] = topic

    db[DB_COLLECTION_NAME].replace_one({'digest': task['digest']}, task, upsert = True)


while True:

    if dedupe_queue_client is not None:

        message = dedupe_queue_client.get_message()

        if message is not None:
            try:
                handle_message(message)
            except Exception as e:
                print e
                pass

        dedupe_queue_client.sleep(SLEEP_TIME_IN_SECONDS)