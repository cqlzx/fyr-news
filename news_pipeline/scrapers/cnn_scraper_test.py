import cnn_scraper

NEWS_URL = 'http://www.cnn.com/2017/10/25/politics/trump-russia-sanctions/index.html'
PART_OF_NEWS = 'Since then, the administration has taken some steps to comply with the law'


def test_basic():
    news = cnn_scraper.getNewsFromUrl(NEWS_URL)

    print news
    assert PART_OF_NEWS in news

    print 'CNN news scraper test passed!'


if __name__ == '__main__':
    test_basic()
