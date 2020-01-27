
with open('Photo1.jpg','rb') as photo:
    byte=photo.read()
    
    with open('exePhoto.jpg','w') as fil:
        fil.write(str(byte))
