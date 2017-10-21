import operations

def test_getOneNews_basic():
    news = operations.getOneNews()
    print news
    assert news is not None
    print 'Test get one news passed!'

if __name__ == '__main__':
    test_getOneNews_basic()