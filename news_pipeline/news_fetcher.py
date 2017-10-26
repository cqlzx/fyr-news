import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'scrapers'))

import cnn_scraper
from cloud_amqp_client import CloudAmqpClient

SLEEP_TIME_IN_SECONDS = 5

FYR_NEWS_QUEUE_URL = 'amqp://mlcafzrx:i3YEi-GptkW4ntHLh0mTV_zzc9qs4hGU@donkey.rmq.cloudamqp.com/mlcafzrx'
SCRAPE_TASK_QUEUE = 'fyr-news-scrape-task'
DEDUPE_TASK_QUEUE = 'fyr-news-dedupe-task'

scrape_queue_client = CloudAmqpClient(FYR_NEWS_QUEUE_URL, SCRAPE_TASK_QUEUE)
dedupe_queue_client = CloudAmqpClient(FYR_NEWS_QUEUE_URL, DEDUPE_TASK_QUEUE)


def handle_message(msg):
    if msg is None or not isinstance(msg, dict):
        print 'Invalid message!'
        return

    task = msg
    text = None

    if task['source'] == 'cnn':
        print 'Scaping CNN news'
        text = cnn_scaper.get_news_from_url(task['url'])
    else:
        print 'News source [%s] is not supported' % task['source']

    task['text'] = text
    dedupe_queue_client.send_message(task)


while True:
    if scrape_queue_client is not None:

        message = scrape_queue_client.get_message()

        if message is not None:

            try:
                handle_message(message)
            except Exception:
                print Exception
                pass

        scrape_queue_client.sleep(SLEEP_TIME_IN_SECONDS)
