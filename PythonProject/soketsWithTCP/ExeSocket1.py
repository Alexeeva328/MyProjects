from socket import socket


try:
    sock=socket()
    sock.connect(('localhost',9000))
    sock.send('Hi!'.encode("utf-8"))
    
    data=sock.recv(1024)
    sock.close()
    
    print (data)


finally:
    #camera.close()
    print("End of work with socket")  