import pyjsonrpc

HTTP_HOST = 'localhost'
HTTP_PORT = 4040

class RequestHandler(pyjsonrpc.HttpRequestHandler):

    @pyjsonrpc.rpcmethod
    def add(self, a, b):
        """Test method"""
        return a + b


# Threading HTTP-Server
http_server = pyjsonrpc.ThreadingHttpServer(
    server_address = (HTTP_HOST, HTTP_PORT),
    RequestHandlerClass = RequestHandler
)

print "Starting HTTP server ..."
print "URL: http://%s:%d" % (HTTP_HOST, HTTP_PORT)

http_server.serve_forever()