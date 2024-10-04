from server import TCPServerHandler
import socketserver
#Will eventually implement multiprocessing to allow the running of multiple rooms simultaneously
import multiprocessing
import json


#Very boring right now but will add text command function to create and navigate rooms
if __name__ == "__main__":
    with socketserver.TCPServer(("flippinnublet.com", 5432), TCPServerHandler) as tcpserver:
        tcpserver.serve_forever()