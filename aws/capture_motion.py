
#import the necessary packages
from gpiozero import Button, MotionSensor
from picamera import PiCamera
from time import sleep
from signal import pause
import os
from os import listdir
import threading
import time
from time import sleep
from datetime import datetime

#create objects that refer to a button,
#a motion sensor and the PiCamera
#button = Button(2)
pir = MotionSensor(4)
camera = PiCamera()
lastdt=0
#start the camera
camera.rotation = 180
#camera.start_preview()

#image image names
i = 0


def upload():
    global i
    cam = 11111
    
    picpath="/home/pi/tmp/"
    camera.capture('/home/pi/tmp/image_%s.jpg' % i)

    print("test")
    
    for f in listdir(picpath):
        if f[0] == "i" and f[1] =="m":
            dt = int(time.time())
            newf = picpath + "img_"+str(cam)+"_"+str(dt)+"_"+str(i)+".jpg"
            cmd1 ="sudo mv "+picpath+ f + "  " + newf
            i+=1
            os.system(cmd1)
            cmd = 'sudo s3cmd put FILE ' + newf + ' s3://puneet.camera.photos'
            print(cmd)
            r=os.system(cmd)
            if(r==0):
                cmd='sudo rm '+newf
                os.system(cmd)

#aassign a function that runs when the button is pressed
#button.when_pressed = stop_camera
#assign a function that runs when motion is detected

pir.when_motion =  upload


pause()
