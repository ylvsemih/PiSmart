import RPi.GPIO as GPIO
import time
from pygame import mixer  # Load the popular external library


GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR
GPIO.setup(24, GPIO.IN) #PIR2
#GPIO.setup(22, GPIO.OUT) #BUzzer
counter=0


try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(23):

            #GPIO.output(22, True)
            #time.sleep(0.5) #Buzzer turns on for 0.5 sec
            #GPIO.input(24, False)
            counter=counter+1
            print("counter: ",counter)
            if counter==1:
                print("Motion Detected(1)...")
                namemp3="3.mp3"

            if counter==2:
                print("Motion Detected(2)...")
                mp3iki="2.mp3"
            elif counter==3:
                print("Motion Detected(3)...")
                namemp3 = "Jagshemash.mp3"
            elif counter==4:
                print("Motion Detected(4)...")
                namemp3 = "Doladies.mp3"
            elif counter==5:
                print("Motion Detected(5)...")
                namemp3 = "Bingbong.mp3"
            elif counter==6:
                print("Motion Detected(6)...")
                namemp3 = "Borattheme.mp3"
            elif counter==7:
                print("Motion Detected(7)...")
                namemp3 = "Newwife.mp3"
            elif counter==8:
                print("Motion Detected(8)...")
                namemp3 = "Theresmell.mp3"
            elif counter==9:
                print("Motion Detected(9)...")
                namemp3 = "Mywife.mp3"
            elif counter==10:
                print("Motion Detected(10)...")
                namemp3 = "Heis.mp3"
            elif counter==11:
                print("Motion Detected(11)...")
                namemp3 = "1.mp3"
                mixer.music.stop()
            mixer.init()
            if counter ==1:
                mixer.music.load('/home/pi/mu_code/%s'%namemp3)
            elif counter ==2:
                mixer.music.load('/home/pi/mu_code/%s'%mp3iki)


            mixer.music.play()
            time.sleep(5) #to avoid multiple detection
        if GPIO.input(24):
            print('CANCEL Motion DETECTED!')

            mixer.music.stop()
            time.sleep(5)

        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()