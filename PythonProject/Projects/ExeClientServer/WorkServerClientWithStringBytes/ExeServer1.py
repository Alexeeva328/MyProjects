from socket import socket
sock=socket()
host='localhost'
port=8007
# свяжем сокет с данным хостом  портом с помощю bind
sock.bind((host,port))  #первый элемент-хост, второй -номер любого порта
sock.listen(1)  # where 1-this is maximum set of connecting in queue
conn,addr=sock.accept() # return new socket and adress клента

print ('connected:',addr)
    
while True:
    data=conn.recv(1024) #reading portions of 1024 bytes
    if not data:
        #print("Error! Data not transmission")
        break
    print('Received data:',data)
    #conn.send("Data is here!")
    answ="Received data!"
    conn.send(answ.encode("utf-8"))
conn.close()
conn.close()         
  


