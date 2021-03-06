""" CloudAMQP client """

import json
import pika


class CloudAmqpClient(object):
    """ CloudAMQP Client"""
    def __init__(self, cloud_amqp_url, queue_name):
        """ Init function """
        self.queue_name = queue_name
        self.params = pika.URLParameters(cloud_amqp_url)
        self.params.socket_timeout = 5

        self.connection = pika.BlockingConnection(
            self.params)  # Connect to CloudAMQP
        self.channel = self.connection.channel()  # start a channel
        self.channel.queue_declare(queue=queue_name)  # Declare a queue
        # send a message

    def send_message(self, message):
        """ Send message function """
        self.channel.basic_publish(
            exchange='', routing_key=self.queue_name, body=json.dumps(message))
        print "[x] Message sent to %s: %s" % (self.queue_name, message)
        # self.connection.close()

    def get_message(self):
        """ Get message function """
        method_frame, header_frame, body = self.channel.basic_get(self.queue_name)    # pylint: disable=unused-variable

        if method_frame:
            print '[x] Message received from %s: %s' % (self.queue_name, body)
            self.channel.basic_ack(method_frame.delivery_tag)
            return json.loads(body)
        else:
            print 'No message received'
            return None

    def sleep(self, seconds):
        """ Sleep function """
        self.connection.sleep(seconds)
