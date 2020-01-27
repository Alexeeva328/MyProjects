from picamera import PiCamera,Color
from datetime import datetime
from time import sleep

try:
    camera= PiCamera() #создаем экземпляр
    camera.annotate_background=Color("teal")
    camera.annotate_foreground=Color("lightpink")
    #for exposure in range(3):
    camera.annotate_text=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.annotate_text_size=55
        #camera.exposure_mode="backlight"
    #camera.awb_mode='sunlight'
    #camera.rotation=180
        #camera.annotate_text="Exp: %s" % exposure
    #camera.capture( '/root/Pictures/Example1/PhotoInNight.jpg')
    camera.capture( '/root/Pictures/Example1/PhotoInDay.jpg')
        #camera.capture( '/root/Pictures/Example1/pic0%s.jpg' %exposure)
        #sleep(2)
    
finally:
    camera.close()
    print("End of program")
