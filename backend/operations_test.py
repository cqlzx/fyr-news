""" Test for operations """

import operations
import os
import sys

from sets import Set

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client


def test_one_news_basic():
    """ Basic test for getting one news """
    news = operations.get_one_news()
    print news
    assert news is not None
    print 'Test get one news passed!'


def test_get_news_summaries_for_user_basic():
    news = operations.get_news_summaries_for_user('test', 1)
    print news
    assert len(news) > 0
    print 'test_get_news_summaries_for_user_basic success!'


def test_get_news_summaries_for_user_pagination():
    news_page_1 = operations.get_news_summaries_for_user('test', 1)
    news_page_2 = operations.get_news_summaries_for_user('test', 2)

    assert len(news_page_1) > 0
    assert len(news_page_2) > 0

    # Assert that there is no dupe news in two pages.
    digests_page_1_set = Set([news['digest'] for news in news_page_1])
    digests_page_2_set = Set([news['digest'] for news in news_page_2])
    assert len(digests_page_1_set.intersection(digests_page_2_set)) == 0

    print 'test_get_news_summaries_for_user_pagination passed!'


if __name__ == '__main__':
    test_one_news_basic()
    test_get_news_summaries_for_user_basic()
    test_get_news_summaries_for_user_pagination()
