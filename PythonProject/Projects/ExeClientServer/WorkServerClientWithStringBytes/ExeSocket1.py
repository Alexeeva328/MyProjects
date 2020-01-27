from socket import socket
host='localhost'
port=8007
try:
    sock=socket()
    sock.connect((host,port))
    st='Hi!'
    #sock.send(st.encode())
    sock.send(st.encode("utf-8"))
    #sock.send(st.encode("utf-8"))
    data=sock.recv(1024)
    sock.close()
    
    print (data)


finally:
    #camera.close()
    print("End of work with socket")  