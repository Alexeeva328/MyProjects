from socket import socket, gethostbyname, AF_INET, SOCK_STREAM,MSG_WAITALL
import picamera
import copy
from datetime import datetime
import sys
import json
from io import BytesIO
from PIL import Image
from array import *

def TakePhoto():
    camera= picamera.PiCamera()
    filename=datetime.today()
    #print(filename)
    camera.annotate_background=picamera.Color("teal")
    camera.annotate_foreground=picamera.Color("lightpink")
    camera.annotate_text=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.annotate_text_size=55
    #camera.resolution(100,100)
    camera.capture( '/home/pi/Pictures/Test/Photo1.jpg',resize=(200,200))
    camera.close()

def EncodingPhoto(sizePhoto,img_data):
    #get string
    img_data=None
    with open('/home/pi/Pictures/Test/Photo1.jpg','rb') as phB:
        img_data=phB.read()
        sizePhoto=len(img_data)
    return sizePhoto,img_data

#def ParseInputData(data):
#    jsonStringInputData=json.dumps(data.decode("utf-8"))
#    strOrder=jsonStringInputData[4:6] #get symbols from 4 to 6
#    print(strOrder)
    
def CreateOnePacket(sizePhoto,img_data):
    #dataListImage=list(img_data)
    payload_size=500
    #dataArrayPacketsStrings=[] 
    print("%im data[:2]^ ",img_data[0:4])
    dataJSON = {
            "headerStart": 10,
            "IPSource":"",
            "lengthCurrentData":0,
            "Data":"",
            #"IPTarget":
            "CRC": 0,
            "headerEnd": 11
            }
    
    packetRange=0
    realPart=0
    countPackets=sizePhoto % payload_size
    print("%%%%   ",sizePhoto%payload_size)

    if countPackets != 0:
        realPart = sizePhoto // payload_size #only whole part without remainder
        packetRange = realPart + 1
    else:
        packetRange = sizePhoto // payload_size

    dataArrayPacketsStrings=[[0] for i in range(packetRange)] 
    

    for num in range( packetRange ):
        #OneJSON=CreateOnePacket(img_data)
        dataDeepCopy = copy.deepcopy( dataJSON )
        dataDeepCopy[ "IPSource" ] = gethostbyname( "pi" )

        dataDeepCopy[ "lengthCurrentData" ] = payload_size
        
        payload_begin_byte = num * payload_size
        payload_end_byte = payload_size + payload_size * num
        

        dataListImage = list( img_data[ payload_begin_byte:payload_end_byte ] ) #in hex format
        dataDeepCopy[ "Data" ] = dataListImage
        
        stringJson = json.dumps( dataDeepCopy ) #get string json
        
        dataArrayPacketsStrings[num]=stringJson
    return dataArrayPacketsStrings
           

def PackingPictures(sizePhoto,img_data):
    print("%im data[:2]^ ",img_data[0:4])
    dataJSON = {
            "headerStart": 10,
            "IPTarget":"34",
            "ProtocolIdentifier":2,
            "IPSource":"35",
            "lengthCurrentData":0,
            "headerCRC":0,
            "Data":"",
            #"IPTarget":
            "CRC": 0,
            "headerEnd": 11
            }
    
    packetRange=0
    realPart=0

    dataDeepCopy = copy.deepcopy( dataJSON )
    #dataDeepCopy[ "IPSource" ] = gethostbyname( "pi" )
        
    dataDeepCopy[ "lengthCurrentData" ] = sizePhoto
    
    #dataDeepCopy[ "headerCRC" ]=
    
    dataDeepCopy[ "Data" ] = list(img_data)
    #print("dataDeepCopy[ 'Data' ]:",dataDeepCopy[ "Data" ])
    stringJson= json.dumps( dataDeepCopy ) #get string json
        
    return stringJson
        

def GetPacks():
    TakePhoto()
    a=0
    b=0
    img_data=0
    stringJson=""
    dataArrayPacketsStrings=[]
    
    sizePhoto,img_data=EncodingPhoto(a,b)
    
    stringJson=PackingPictures(sizePhoto,img_data)
    return stringJson
    

def main():
    PORT_NUMBER = 9000
    SIZE = 1024
    
    hostName='0.0.0.0'
    print(hostName)
    
    mySocket = socket(AF_INET, SOCK_STREAM,0)
    mySocket.bind((hostName,PORT_NUMBER))
    
    while True:
        
        mySocket.listen(5)  # where 1-this is maximum set of connecting in queue
        print("Server is running, please, press ctrl+c to stop\n")
        #print("Server is running, please, press ctrl+c to stop, or if you write: ex=q , then you can go out\n")
        conn,addr=mySocket.accept() # return new socket and adress 
        print ('connected:',addr)
        print("Server is up\n")
        #if ex=='q' or ex=='Q':
         #   print("Goodbye!")
          #  break
        #data = conn.recv(SIZE,MSG_WAITALL).decode()
        stringJson=""
        #dataArrayPacketsStrings=[]
          
        data = conn.recv(SIZE)
        if not data:
            sleep(1)
            #break
        else:
            Pack=GetPacks()
            #print ("\n onePacket.encode('utf-8') :  ", Pack)
            print("With decode input data:",data.decode("utf-8"))
            a=0
            #answer=conn.send(sizePhoto.encode("utf-8"))
            #answer=conn.send("hi, friend!".encode("utf-8"))
            
            #dataImage=json.loads(Pack.read())
            dataImage = json.loads( Pack )
            
            headerData=str(dataImage[ "headerStart" ]) + str(dataImage["IPTarget"])+str(dataImage[ "ProtocolIdentifier" ]) + str(dataImage["IPSource"]+ str(dataImage["lengthCurrentData"]) ) 
            dataImage["headerCRC"] = len(headerData)
            dataImage["CRC"] = dataImage["headerCRC"] + len(dataImage["Data"] )
            print("\n len(headerData)  : ",len(headerData))
            headerData += str(dataImage["headerCRC"])
            #headerData=join( str(dataImage[ "headerStart" ]),str(dataImage[ "IPSource" ]) )
            #print ("header start ",Pack[ "headerStart" ])
            print ("\n headerData ",headerData)
            
            answer=conn.send(headerData.encode("utf-8"))
            
            req=conn.recv(1)
            #print ("\n headerData ",headerData)
            if req == b'1':
                #conn.send((str (dataImage["CRC"] ) ).encode("utf-8"))
                #conn.resv(1)
                conn.send( ( str (dataImage["Data"] ) + str (dataImage["CRC"] ) + str (dataImage["headerEnd"] ) ).encode("utf-8") )
                print ( "\n \n Data sended \n" )
            
            #for numPack in range( len(dataArrayPacketsStrings) ):
            #    answer=conn.send(dataArrayPacketsStrings[numPack].encode("utf-8"))
        #answer=conn.send(json_string.encode("utf-8"))
        conn.close()
    sys.exit()
    
    
main()





