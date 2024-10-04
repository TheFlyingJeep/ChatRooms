import socket, sys


#Create socket, connect it to specific port on flippinnublet (Should probably do error handling)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("flippinnublet.com", 5432))
    data = "Testing out sockets"
    #Byte data go brr send and then just rereceive, will also receive any message from anyone connected to the TCPServer once it permanently listens
    sock.sendall(bytes(data+"\n", "utf-8"))
    received = str(sock.recv(1024), "utf-8")
    print("Sent: {}".format(data))
    print("Received: {}".format(received))