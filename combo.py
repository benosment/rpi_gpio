#! /usr/bin/python

### note: script must be run as root

import RPi.GPIO as GPIO
import time

# use the on-board Broadcom chip's signal name for each pin
# instead of the physical layout
GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN)
GPIO.setup(26, GPIO.OUT)

led_on = False
count = 0

while True:
    input_value = GPIO.input(24)
    if input_value:
        count += 1
        print("Button pressed %d times." % count)
        # toggle LED
        led_on = not led_on
        if led_on:
            print("Turning LED on")
            GPIO.output(26, GPIO.HIGH)
        else:
            print("Turning LED off")            
            GPIO.output(26, GPIO.LOW)
        time.sleep(0.3)            
    time.sleep(0.3)
