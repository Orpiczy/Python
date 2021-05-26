import RPi.GPIO as gpio
import w1thermsensor
from time import *

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

gpio.setup(26, gpio.OUT)
gpio.output(26, gpio.LOW)

temp_max = 29.00
sensor = w1thermsensor.W1ThermSensor()
try:
    while True:
        temp = sensor.get_temperature()
        print(temp)
        if temp > temp_max:
            gpio.output(26, gpio.HIGH)
            print("Alarm")
        else:
            gpio.output(26, gpio.LOW)
        sleep(1)
except KeyboardInterrupt:
    gpio.output(21, gpio.HIGH)
    print("Koniec")
    gpio.cleanup()
