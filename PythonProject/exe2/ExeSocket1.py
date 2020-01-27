import sys
from socket import socket, AF_INET, SOCK_DGRAM


def main():
    SERVER_IP = '192.168.0.103'
    PORT_NUMBER = 5000
    SIZE = 1024
    print("start")

    mySocket = socket(AF_INET, SOCK_DGRAM)
    i = 0
    while i < 5:
        myMessage = input(">")
        mySocket.sendto(myMessage.encode('utf-8'), (SERVER_IP, PORT_NUMBER))
        i = i + 1
    myMessage1 = input(">>")
    mySocket.sendto(myMessage1.encode('utf-8'), (SERVER_IP, PORT_NUMBER))

    sys.exit()

main()
