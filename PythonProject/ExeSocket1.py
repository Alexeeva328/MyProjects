import sys
from socket import socket, AF_INET, SOCK_DGRAM


def main():
    SERVER_IP = '192.168.2.51'
    PORT_NUMBER = 5000
    SIZE = 1024
    print("start!")
    #socket.gethostbyname(socket.getfqdn())
    mySocket = socket(AF_INET, SOCK_DGRAM)
    myId=socket.getsockname
    #mySocket.connect((host,port))
    #mySocket.connect((AF_INET, SOCK_DGRAM))
    st='Hi!'
    #mySocket.send(st.encode("utf-8"))
    mySocket.sendto(st.encode('utf-8'), (SERVER_IP, PORT_NUMBER))
    #sock.send(arr)
    data=mySocket.recv(1024)
    sock.close()
    #i = 0
    #while i < 5:
    #    myMessage = input(">")
    #    mySocket.sendto(myMessage.encode('utf-8'), (SERVER_IP, PORT_NUMBER))
    #    i = i + 1
    #myMessage1 = input(">>")
    #mySocket.sendto(myMessage1.encode('utf-8'), (SERVER_IP, PORT_NUMBER))

    sys.exit()

main()
