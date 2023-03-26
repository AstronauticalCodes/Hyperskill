import sys
from socket import socket
from itertools import product


address = (sys.argv[1], int(sys.argv[2]))
lines = []

with open(r'C:\Users\indus\PycharmProjects\Password Hacker1\Password Hacker\task\hacking\passwords.txt') as f:
    lines_1 = f.readlines()

for y in lines_1:
   lines.append(y.strip('\n'))

with socket() as client_socket:
    client_socket.connect(address)
    for x in lines:
        print(x)
        x.replace('\n', '')
        if x.isnumeric():
            convert = int(x)
            data = x.encode()
            client_socket.send(data)
            response = client_socket.recv(1024)
            response = response.decode('utf-8')
            if response == 'Connection success!':
                if x != '':
                    print(x)
                exit()
            elif response == 'Wrong password!':
                continue
            elif response == 'Too many attempts':
                exit()
        else:
            comb = map(''.join, product(*zip(x.lower(), x.upper())))
            for z in range(2 ** len(x)):
                val = next(comb)
                data = val.encode()
                client_socket.send(data)
                response = client_socket.recv(1024)
                response = response.decode()
                if response == 'Connection success!':
                    if val != '':
                        print(val)
                    exit()
                elif response == 'Wrong password!':
                    continue
                elif response == 'Too many attempts':
                    exit()
