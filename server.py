import socketserver
import json


#Server handler class (I could do more with a setup and finish function but I'm way too lazy to rn)
class TCPServerHandler(socketserver.BaseRequestHandler):

    def handle(self):
        #Simply get all data, format it, then send it back to all existing sockets on the server
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data)