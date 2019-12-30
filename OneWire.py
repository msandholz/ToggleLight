#!/usr/bin/env python
#coding: utf8

import os
import glob


base_dir = '/sys/devices/w1_bus_master1/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + 'w1_slave'


print("Result: "+ device_folder)
