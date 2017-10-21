""" Test for operations """

import operations


def test_one_news_basic():
    """ Basic test for getting one news """
    news = operations.get_one_news()
    print news
    assert news is not None
    print 'Test get one news passed!'


if __name__ == '__main__':
    test_one_news_basic()
