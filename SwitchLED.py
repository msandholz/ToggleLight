#!/usr/bin/env python
#coding: utf8

import os
import RPi.GPIO as GPIO
from time import sleep

# 1-wire
#os.system('modprobe w1-gpio')
#os.system('modprobe wi-therm')

#base_dir = '\sys\bus\w1\devices'
#device_folder = glob.glob(base_dir + '28*')[0]
#device_file = device_folder + 'w1_slave'




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