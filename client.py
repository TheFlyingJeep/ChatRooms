import socket, multiprocessing


def listen_thread(sock):
    while 1:
        data = str(sock.recv(1024), "utf-8")
        if data != None and data != "":
            print(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("flippinnublet.com", 5432))
    sock.send(bytes("Connected", "utf-8"))
    receivedConnection = str(sock.recv(1024), "utf-8")
    print(receivedConnection)
    sock_listen = multiprocessing.Process(target=listen_thread, args=(sock,))
    sock_listen.start()
    while 1:
        command = input("Send a message (type /exit to quit): ")
        if command.lower() == "/exit":
            break
        else:
            sock.send(bytes(command, "utf-8"))
    sock_listen.join()
    sock.close()
    exit()