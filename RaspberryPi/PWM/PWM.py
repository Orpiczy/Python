import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

gpio.setup(12, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(26, gpio.IN, pull_up_down=gpio.PUD_UP)

diodeRed = gpio.PWM(12, 50)
diodeGreen = gpio.PWM(16, 50)

duty = 0
diodeRed.start(duty)
diodeGreen.start(duty)
isRising = True
try:
    while True:
        if gpio.input(26) == 0:
            duty = 100 if duty == 0 else 0

        # if isRising:
        #     duty += 10
        #     if duty == 100:
        #         isRising = False
        # else:
        #     duty -= 10
        #     if duty == 0:
        #         isRising = True
        diodeRed.ChangeDutyCycle(duty)
        diodeGreen.ChangeDutyCycle(100 - duty)
        time.sleep(0.5)
except KeyboardInterrupt:
    print('Finish')

diodeRed.stop()
diodeGreen.stop()
gpio.cleanup()
