import socket
import sys

address = (sys.argv[1], int(sys.argv[2]))

with socket.socket() as client_socket:
    client_socket.connect(address)
    data = (sys.argv[3]).encode()
    client_socket.send(data)
    response = client_socket.recv(1024)
    response = response.decode()
    print(response)
