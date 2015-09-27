#! /usr/bin/python

### note: script must be run as root

import RPi.GPIO as GPIO
import time

# use the on-board Broadcom chip's signal name for each pin
# instead of the physical layout
GPIO.setmode(GPIO.BCM)

# configure pin 25 to be output (as oppose to input)
GPIO.setup(25, GPIO.OUT)

while True:
    # turn LED on
    GPIO.output(25, GPIO.HIGH)
    time.sleep(1)
    # turn LED off
    GPIO.output(25, GPIO.LOW)
    time.sleep(1)
