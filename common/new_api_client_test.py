import news_api_client as client

def test_basic():
    articles = client.getNewsBySources()
    print articles
    assert len(articles) > 0
    articles = client.getNewsBySources(sources=['bbc-news'])
    assert len(articles) > 0
    print 'News api test passed!'

if __name__ == '__main__':
    test_basic()