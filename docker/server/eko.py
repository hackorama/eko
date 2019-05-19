"""Simple TCP, HTTP, HTTPS echo server for testing."""
#
# HTTPS needs a server.pem:
#  openssl req -new -x509 -keyout server.pem -out server.pem \
#    -days 365 -nodes -subj "/C=US/ST=CA/L=SF/O=TEST/OU=TEST/CN=TEST"
#
import SimpleHTTPServer
import SocketServer
import socket
import ssl
import sys
import threading
import time

HOST       = sys.argv[1] if len(sys.argv) > 1 else "0.0.0.0"
HTTP_PORT  = int(sys.argv[2]) if len(sys.argv) > 2 else  8080
HTTPS_PORT = int(sys.argv[3]) if len(sys.argv) > 3 else 8443
TCP_PORT   = int(sys.argv[4]) if len(sys.argv) > 4 else 5000
DEBUG      = int(sys.argv[5]) if len(sys.argv) > 5 else 0
NAME       = sys.argv[6] if (len(sys.argv) > 6 and sys.argv[5]) else "EKO_SERVER_%s%s%s%s" % (HOST, \
                ("_HTTP:%s" % HTTP_PORT) if HTTP_PORT else "", \
                ("_HTTPS:%s" % HTTPS_PORT) if HTTPS_PORT  else "", \
                ("_TCP:%s" % TCP_PORT) if TCP_PORT else "")

class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        if DEBUG > 0:
            self.wfile.write("CLIENT HOST      : %s:%s\n" % (self.client_address[0], self.client_address[1]))
            self.wfile.write("REQUEST_TYPE PATH: %s %s\n" % (self.command, self.path))
            self.wfile.write("SERVER VERSION   : %s\n" % self.server_version)
            self.wfile.write("REQUEST VERSION  : %s\n" % self.request_version)
            self.wfile.write("PROTOCOL VERSION : %s\n" % self.protocol_version)
            self.wfile.write("HEADERS          : %s\n" % self.headers)
        self.wfile.write(NAME)
        self.wfile.write("\n")
    def log_message(self, format, *args):
        return

def serve(server):
    try:
        server.serve_forever()
    finally:
        server.socket.close()

print("Starting %s on %s" % (NAME, HOST))

if HTTP_PORT:
     print("HTTP server on port %d" % HTTP_PORT)
     httpd = SocketServer.TCPServer((HOST, HTTP_PORT), GetHandler)
     httpd_server_thread = threading.Thread(target=serve, args=[httpd])
     httpd_server_thread.daemon = True
     httpd_server_thread.start()

if HTTPS_PORT:
    print("HTTPS server on port %d" % HTTPS_PORT)
    httpds = SocketServer.TCPServer((HOST, HTTPS_PORT), GetHandler)
    httpds.socket = ssl.wrap_socket (httpds.socket, certfile='./server.pem', server_side=True)
    httpds_server_thread = threading.Thread(target=serve, args=[httpds])
    httpds_server_thread.daemon = True
    httpds_server_thread.start()

if TCP_PORT:
    print("TCP server on port %d" % TCP_PORT)
    sock = None
    connection = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (HOST, TCP_PORT)
        sock.bind(server_address)
        sock.listen(1)
        while True:
            connection, client_address = sock.accept()
            print("Connection from: %s:%s" % (client_address[0], client_address[1]))
            connection.sendall("%s\n" % NAME)
            while True:
                data = connection.recv(1024)
                print("%s %s: %s" % (client_address[0], client_address[1], data))
                if data:
                    connection.sendall(data)
                else:
                    break
    except KeyboardInterrupt:
        pass # passed to finally
    finally:
        if connection:
            connection.close()
        sock.close()
else:
    try:
        while True:
            time.sleep(0.2)
    except KeyboardInterrupt:
        pass # expected to exit on ctrlc, ignore traceback
