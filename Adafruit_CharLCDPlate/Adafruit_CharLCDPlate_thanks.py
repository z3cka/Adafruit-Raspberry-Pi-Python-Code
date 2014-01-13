#!/usr/bin/python
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from time import sleep

# Initialize LCD plate
lcd = Adafruit_CharLCDPlate()

# Clear display
lcd.clear()

# Put message in a variable
message = "Thanks Grant & Bebe! Love Domnic & Trent"

# Output "Thank You" message
lcd.message(message)
# Calc how many spaces to move
move = len(message) - 16

# Loop until any button is pressed
loop = 1
while True:
  # Wait one second
  sleep(1)
  # Scroll display
  for x in range(0,move):
    lcd.scrollDisplayLeft()
    sleep(0.15)
  # Wait half a second
  sleep(0.5)
  # Scroll display back
  for x in range(0, move):
    lcd.scrollDisplayRight()
    sleep(0.08)
  if lcd.buttonPressed():
    loop = 0
  loop += 1

