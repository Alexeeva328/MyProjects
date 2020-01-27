from socket import socket
import numpy as np
from PIL import Image

img=Image.open('pss3.jpg')
img.load()
arr=np.asarray(img,dtype='uint8')#convert image to pixel array 
#print (arr.size())

host='localhost'
port=8008
try:
    sock=socket()
    sock.connect((host,port))
    st='Hi!'
    #sock.send(st.encode())
    #sock.send(st.encode("utf-8"))
    sock.send(arr)
    data=sock.recv(1024)
    sock.close()
    
    print (data)


finally:
    #camera.close()
    print("End of work with socket")  