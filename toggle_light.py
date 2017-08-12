#!/usr/bin/env python
#coding: utf8

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

# Button
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# Check Light status
GPIO.setup(9, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# Relais on/off
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, False)

# Light on/off
GPIO.setup(8, GPIO.OUT)
GPIO.output(8, False)

print("Toggle_light service started!")

while True:
	led = GPIO.input(9)
	
	GPIO.wait_for_edge(11, GPIO.RISING)
	sleep(0.05)

	GPIO.output(8, not led)
	
	GPIO.wait_for_edge(11, GPIO.FALLING)
	sleep(0.05)