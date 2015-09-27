#! /usr/bin/python

### note: script must be run as root

import RPi.GPIO as GPIO

# use the on-board Broadcom chip's signal name for each pin
# instead of the physical layout
GPIO.setmode(GPIO.BCM)

# configure pin 25 to be output (as oppose to input)
GPIO.setup(25, GPIO.OUT)

# turn LED on
GPIO.output(25, GPIO.HIGH)

# turn LED off
GPIO.output(25, GPIO.LOW)
