from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys


def main():
    PORT_NUMBER = 5000
    SIZE = 1024
    hostName = gethostbyname('0.0.0.0')
    mySocket = socket(AF_INET, SOCK_DGRAM)
    mySocket.bind((hostName, PORT_NUMBER))
    print("Server is up\n")
    while True:
        (data, addr) = mySocket.recvfrom(SIZE)
        print(data.decode("utf-8"))
    sys.exit()
   
main()
