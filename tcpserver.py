#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8888

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()

    print(f"Received connexion from {str(address)}")

    message = "Welcome ! Thank you for connecting to the server"

    clientsocket.send(message.encode("ascii"))

    clientsocket.close()