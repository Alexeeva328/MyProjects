from picamera import PiCamera,Color
from datetime import datetime

camera= PiCamera()
# take a series of shots without delay
#for i in range(3):
filename=datetime.today()
    #filename2="{0:%Y}-{0:%m}-{0:%d}".format(now)
    #camera.capture( '/root/Pictures/Example1/{0:%Y}-{0:%m}-{0:%d}'.format(now).jpg)
print(filename)
camera.annotate_background=Color("teal")
camera.annotate_foreground=Color("lightpink")
camera.annotate_text=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
camera.annotate_text_size=55
camera.capture( '/root/Pictures/Example1/PhotoWithDataToday.jpg')