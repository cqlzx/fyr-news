from cloudAMQP_client import CloudAMQPClient

AMQP_URL = 'amqp://mlcafzrx:i3YEi-GptkW4ntHLh0mTV_zzc9qs4hGU@donkey.rmq.cloudamqp.com/mlcafzrx'
QUEUE_NAME = 'test'

def test_basic():
    client = CloudAMQPClient(AMQP_URL, QUEUE_NAME)
    message_sent = {'test': 'test1'}
    client.sendMessage(message_sent)
    message_received = client.getMessage()
    assert message_sent == message_received
    print 'test passed!'

if __name__ == '__main__':
    test_basic()