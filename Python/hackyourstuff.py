import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)

while True:
    if (GPIO.input(17)):
        print("on")
        GPIO.output(18, GPIO.HIGH)

    else:
        GPIO.output(18, GPIO.LOW)

#while False:
 #   if (GPIO.input(17)):
  #      GPIO.output(18, GPIO.LOW)
