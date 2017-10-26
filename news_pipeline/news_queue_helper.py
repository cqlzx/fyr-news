import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import news_api_client
from cloud_amqp_client import CloudAmqpClient


FYR_NEWS_QUEUE_URL = 'amqp://mlcafzrx:i3YEi-GptkW4ntHLh0mTV_zzc9qs4hGU@donkey.rmq.cloudamqp.com/mlcafzrx'
FYR_NEWS_QUEUE_NAME = 'fyr-news-api-news'


def clear_queue(queue_url, queue_name):
    cloud_amqp_client = CloudAmqpClient(queue_url, queue_name)

    num_of_messages = 0

    while True:
        message = cloud_amqp_client.get_message()

        if message is None:
            print 'Queue helper cleared %d messages' % num_of_messages
            return

        num_of_messages += 1


if __name__ == '__main__':
    clear_queue(FYR_NEWS_QUEUE_URL, FYR_NEWS_QUEUE_NAME)