from socket import socket, gethostbyname, AF_INET, SOCK_STREAM,MSG_WAITALL
import sys


def main():
    PORT_NUMBER = 9000
    SIZE = 1024
    #hostName = gethostbyname('0.0.0.0')
    #AF_INET for network protokol IPv4
    # свяжем сокет с данным хостом  портом с помощю bind
    hostName='localhost'
    
    mySocket = socket(AF_INET, SOCK_STREAM)
    mySocket.bind((hostName,PORT_NUMBER))  #первый элемент-хост, второй -номер любого порта
    mySocket.listen(1)  # where 1-this is maximum set of connecting in queue
    conn,addr=mySocket.accept() # return new socket and adress клента
    print ('connected:',addr)
    print("Server is up\n")
    while True:
        #data = conn.recv(SIZE,MSG_WAITALL).decode()
        data = conn.recv(SIZE)
        print(data.decode("utf-8"))
    sys.exit()
    conn.close()
main()
