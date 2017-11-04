import os
import sys

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client
import news_topic_modeling_service_client

if __name__ == '__main__':
    db = mongodb_client.get_db()
    cursor = db['test-news'].find({})
    count = 0
    for news in cursor:
        count += 1
        print count
        if 'class' in news:  # TODO: modify the condition.
            print 'Populating classes...'
            title = news['title']
            if title is None:
                title = news['description']
            topic = news_topic_modeling_service_client.classify(title)
            news['class'] = topic
            db['test-news'].replace_one({'digest': news['digest']}, news, upsert=True)