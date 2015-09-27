#! /usr/bin/python

### note: script must be run as root

import RPi.GPIO as GPIO
import time

# use the on-board Broadcom chip's signal name for each pin
# instead of the physical layout
GPIO.setmode(GPIO.BCM)

# configure pin 24 to be input (as oppose to output)
GPIO.setup(24, GPIO.IN)

count = 0

while True:
    input_value = GPIO.input(24)
    if input_value:
        count += 1
        print("Button pressed %d times." % count)
        time.sleep(0.3)
    time.sleep(0.1)
