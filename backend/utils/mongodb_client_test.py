import mongodb_client as client

# Start mongodb before test.
def test_basic():
    db = client.get_db('test')
    db.test.drop()
    assert db.test.count() == 0

    db.test.insert({'test': 1})
    assert db.test.count() == 1

    db.test.drop()
    assert db.test.count() == 0

    print 'basic test passed!'

if __name__ == '__main__':
    test_basic()