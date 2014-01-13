#!/usr/bin/python
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize LCD plate
lcd = Adafruit_CharLCDPlate()

# Clear display
lcd.clear()

# Output "Thank You" message
lcd.message("Thx Grant & Bebe \n" +
            "Love Dom & Trent")

