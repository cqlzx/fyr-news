""" CloudAMQP client test """

from cloud_amqp_client import CloudAmqpClient

AMQP_URL = 'amqp://mlcafzrx:i3YEi-GptkW4ntHLh0mTV_zzc9qs4hGU@donkey.rmq.cloudamqp.com/mlcafzrx'
QUEUE_NAME = 'test'


def test_basic():
    """ Basic test for cloudAMQP"""
    client = CloudAmqpClient(AMQP_URL, QUEUE_NAME)
    message_sent = {'test': 'test1'}
    client.send_message(message_sent)
    message_received = client.get_message()
    assert message_sent == message_received
    print 'test passed!'


if __name__ == '__main__':
    test_basic()
