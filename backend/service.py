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

# Threading HTTP-Server
HTTP_SERVER = pyjsonrpc.ThreadingHttpServer(
    server_address=(HTTP_HOST, HTTP_PORT),
    RequestHandlerClass=RequestHandler
)

print "Starting HTTP server ..."
print "URL: http://%s:%d" % (HTTP_HOST, HTTP_PORT)

HTTP_SERVER.serve_forever()
