#!/usr/bin/python
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from subprocess import *
from time import sleep
import re

# Initialize LCD plate
lcd = Adafruit_CharLCDPlate()
# Clear display
lcd.clear()
# pipe result with command
i = Popen("ip addr show eth0", shell=True, stdout=PIPE)
ips = i.communicate()[0]
# get ip with regex from string, returns array
ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', ips )
# output first item in array
lcd.message(ip[0])

