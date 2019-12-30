#!/usr/bin/env python
#coding: utf8

import os
import RPi.GPIO as GPIO
from time import sleep


# GPIO settings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Button
btn = 18
GPIO.setup(btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# Check Light status
status = 24
GPIO.setup(status, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# Light on/off
light = 25
GPIO.setup(light, GPIO.OUT)
GPIO.output(light, False)

print("SwitchLED service started!")

while True:
	led = GPIO.input(status)
	
	GPIO.wait_for_edge(btn, GPIO.RISING)
	sleep(0.05)

	GPIO.output(light, not led)
	
	GPIO.wait_for_edge(btn, GPIO.FALLING)
	sleep(0.05)