import RPi.GPIO as GPIO
import time
import signal
import sys

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

def allLightsOff(signal, frame):
    GPIO.output(9, False)
    GPIO.output(10, False)
    GPIO.output(11, False)
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, allLightsOff)

# Loop forever
while True: 
    # Red 
    GPIO.output(9, True) 
    time.sleep(3)
  
    # Red and amber 
    GPIO.output(10, True) 
    time.sleep(1)
  
    # Green 
    GPIO.output(9, False) 
    GPIO.output(10, False) 
    GPIO.output(11, True) 
    time.sleep(5) 
 
    # Amber 
    GPIO.output(11, False) 
    GPIO.output(10, True) 
    time.sleep(2) 
 
    # Amber off 
    GPIO.output(10, False)

