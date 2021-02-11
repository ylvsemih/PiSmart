import RPi.GPIO as GPIO
import time
from pygame import mixer  # Load the popular external library


GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR
#GPIO.setup(24, GPIO.OUT) #BUzzer

try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(23):
            #GPIO.output(24, True)
            time.sleep(0.5) #Buzzer turns on for 0.5 sec
            #GPIO.input(24, False)
            print("Motion Detected...")
            

            mixer.init()
            mixer.music.load('/home/pi/mu_code/1.mp3')
            mixer.music.play()
            
            time.sleep(5) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()