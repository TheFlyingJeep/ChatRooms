from server import TCPServerHandler
import socketserver
#Will eventually implement multiprocessing to allow the running of multiple rooms simultaneously
import multiprocessing
import json


if __name__ == "__main__":
    with socketserver.TCPServer(("flippinnublet.com", 5432), TCPServerHandler) as tcpserver:
        tcpserver.serve_forever()