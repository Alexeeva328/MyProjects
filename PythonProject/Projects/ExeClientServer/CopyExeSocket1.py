from socket import socket


try:
    sock=socket()
    sock.connect(('localhost',9090))
    sock.send('Hi!')
    
    data=sock.recv(1024)
    sock.close()
    
    print (data)


finally:
    #camera.close()
    print("End of work with socket")  