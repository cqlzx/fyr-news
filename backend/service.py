""" Backend Service """

import pyjsonrpc
import operations

HTTP_HOST = 'localhost'
HTTP_PORT = 4040


class RequestHandler(pyjsonrpc.HttpRequestHandler):
    """ RPC Request Handler"""

    @pyjsonrpc.rpcmethod
    def add(self, num1, num2):  # pylint: disable=no-self-use
        """Test method"""
        return num1 + num2

    @pyjsonrpc.rpcmethod
    def get_one_news(self):   # pylint: disable=no-self-use
        """ Get one news from mongoDB"""
        return operations.get_one_news()

    @pyjsonrpc.rpcmethod
    def get_news_summaries_for_user(self, user_id, page_num):   # pylint: disable=no-self-use
        """ Get news summaries for user"""
        print 'get summaries for user is called! with %s and %s' % (user_id, page_num)
        return operations.get_news_summaries_for_user(user_id, page_num)

    @pyjsonrpc.rpcmethod
    def log_news_click_for_user(self, user_id, news_id):   # pylint: disable=no-self-use
        """ log news click for user"""
        print 'log news click for user is called with %s and %s' % (user_id, news_id)
        return operations.log_news_click_for_user(user_id, news_id)


# Threading HTTP-Server
HTTP_SERVER = pyjsonrpc.ThreadingHttpServer(
    server_address=(HTTP_HOST, HTTP_PORT),
    RequestHandlerClass=RequestHandler
)

print "Starting HTTP server ..."
print "URL: http://%s:%d" % (HTTP_HOST, HTTP_PORT)

HTTP_SERVER.serve_forever()
