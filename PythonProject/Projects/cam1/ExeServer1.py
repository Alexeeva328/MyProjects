from socket import socket
sock=socket()
host='localhost'
port=8007
# свяжем сокет с данным хостом  портом с помощю bind
sock.bind((host,port))  #первый элемент-хост, второй -номер любого порта, для прмера взяла слайный 9090 порт
sock.listen(1)  # where 1-this is maximum set of connecting in queue
conn,addr=sock.accept() # return new socket and adress клента

print ('connected: %s',addr)
    
while True:
    data=conn.recv(1024) #reading portions of 1024 bytes
    if not data:
        #print("Error! Data not transmission")
        break
    print('Received data: %s')
    #conn.send("Data is here!")
    conn.send("Received data!")
conn.close()
conn.close()
          
  

