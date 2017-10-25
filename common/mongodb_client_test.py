""" Test for mongodb client """

import mongodb_client as client


# Start mongodatabase before test.
def test_basic():
    """ basic test for mongoDB """
    database = client.get_db('test')
    database.test.drop()
    assert database.test.count() == 0

    database.test.insert({'test': 1})
    assert database.test.count() == 1

    database.test.drop()
    assert database.test.count() == 0

    print 'MongoDB client test passed!'


if __name__ == '__main__':
    test_basic()
