from picamera import PiCamera
from time import sleep

camera= PiCamera()
# take photo
camera.capture('/root/Pictures/Example1/PHOTO3.jpg')
# take a series of shots without delay
for i in range(3):
    camera.capture('/root/Pictures/Example1/cicle%s.jpg' % i)
    

#take photo with annotation text
camera.annotate_text="25.11.2019 14:52"

# take photo with effect and with rotation
#camera.image_effect='colorswap'
camera.rotation=180
camera.capture('/root/Pictures/Example1/effect5.jpg')

camera.annotate_text=""
# take photo
camera.resolution=(100,100)
camera.capture('/root/Pictures/Example1/pss3.jpg')