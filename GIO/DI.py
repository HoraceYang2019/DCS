'''
https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
'''
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

DI0Pin = 32   # GPIO12

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(DI0Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Set pin 10 to be an input pin and set initial value to be pulled low (off)
while True: # Run forever
    if GPIO.input(DI0Pin) == GPIO.HIGH:
        print("Button was pushed!")