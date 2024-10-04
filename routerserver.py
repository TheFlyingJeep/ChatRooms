import socketserver, json
import serverhandler


#The server you will originally connect to
#It will reroute you to either an existing server or create a new server instance and connect to it
class RouterServerHandler(socketserver.BaseRequestHandler):

    def setup(self) -> None:
        self.commands = {
            "connect": self.connection(self.request)
        }
        return super().setup()
    
    def handle(self):
        self.data = self.request.recv(1024).strip()
        if str(self.data) in self.commands:
            self.commands[str(self.data)]
        else:
            print("{}: ".format(self.client_address[0] + str(self.data)))
            self.request.send(bytes("received", "utf-8"))
        
    def connection(self, request):
        print("{} has connected".format(self.client_address[0]))
        request.send(bytes("connected", "utf-8"))
        
        

if __name__ == "__main__":
    with socketserver.TCPServer(("flippinnublet.com", 5432), RouterServerHandler) as server:
        server.serve_forever()