#!/usr/bin/python
import RPi.GPIO as GPIO  #not supported by windows
from time import sleep

# Use physical pin numbers
GPIO.setmode(GPIO.BOARD)
# Set up header pin 12 (GPIO18) as an input
ledPin = 12
print ('Setup LED pin')
GPIO.setup(ledPin, GPIO.OUT)

print ('Starting... ')
while True:
  print ('LED on')
  GPIO.output(ledPin, False)
  sleep(1)
  print ('LED off')
  GPIO.output(ledPin, True)
  sleep(1)
