
#import the necessary packages
from gpiozero import Button, MotionSensor
from picamera import PiCamera
from time import sleep
from signal import pause
import os

#create objects that refer to a button,
#a motion sensor and the PiCamera
#button = Button(2)
pir = MotionSensor(4)
camera = PiCamera()

#start the camera
camera.rotation = 180
#camera.start_preview()

#image image names
i = 0

#stop the camera when the pushbutton is pressed
def stop_camera():
    camera.stop_preview()
    #exit the program
    exit()

#take photo when motion is detected
def take_photo():
    global i
    i = i + 1
    camera.capture('/home/pi/Desktop/image_%s.jpg' % i)
    print('A photo has been taken')
    
    cmd= 's3cmd put FILE /home/pi/Desktop/image_' + str(i)  + '.jpg  s3://puneet.camera.photos'
    os.system(cmd)
    sleep(3)
    cmd= 'rm /home/pi/Desktop/image_'+str(i) +'.jpg'
    os.system(cmd)

#assign a function that runs when the button is pressed
#button.when_pressed = stop_camera
#assign a function that runs when motion is detected
pir.when_motion = take_photo


pause()
