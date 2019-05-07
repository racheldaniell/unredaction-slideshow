# Part 1 of the unredaction project

# this script provides the motion sensor trigger for unredact script
# two PIR sensors are connected to the raspberry pi on GPIO pins as defined below and in Fritzing diagram
# based on movement this script calls the image manipulation script as a subprocess
# note both this script and image script must be in same folder

# import libraries needed for this script
# set things up for the pi to read the sensor input
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#import what is needed to have this script trigger other script
import subprocess

# tell python script which pins the data legs of the sensors are connected to
pir_1 = 24 #GPIO pin 24 - warm tone wires PIR
pir_2 = 23 #GPIO pin 23 - cool tone wires PIR
# I named these for wire color for clarity but they could function as left eye/right eye too
# note this versionn of the project only utilizes 1 eye/sensor
# the 2nd sensor here was kept in the code as a potential template for future 2-sensor projects and to test sensor range

GPIO.setup(pir_1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(pir_2, GPIO.IN, GPIO.PUD_DOWN)

current_state = 0

# note the print messages below become covered up with image once the first motion launches the subprocess
while True:
    try:
        time.sleep(0.1)
        current_state_1 = GPIO.input(pir_1)
        current_state_2 = GPIO.input(pir_2)
        if current_state_1 == 1:
          print("WARM EYE SAW YOU!!  [GPIO sensor 1 pin %s is %s]" % (pir_1, current_state_1)) # motion detected eye 1
          # now run the unredaction image processing script as a subprocess
          imageshow = subprocess.call(['python', 'redact_unredact_doc.py'])
          time.sleep(0.7) # pause
        elif current_state_1 == 0:
            print("no motion detected - warm eye")
            time.sleep(0.7)
        if current_state_2 == 1:
          print("COOL EYE SAW YOU!!  [GPIO sensor 2 pin %s is %s]" % (pir_2, current_state_2)) # motion detected eye 2
          # for this eye the current project does not trigger a subprocess, but it used for sensor range testing
          time.sleep(0.3) # pause
        elif current_state_2 == 0:
            print("no motion detected - cool eye")
            time.sleep(0.3)
    except KeyboardInterrupt:
        GPIO.cleanup()
       
