import RPi.GPIO as GP
import time

GP.setmode(GP.BOARD)

red=9
yellow=13
green=15

GP.setup(red,GP.OUT)
GP.setup(yellow,GP.OUT)
GP.setup(green,GP.OUT)

while True:
    GP.output(red,True)
    sleep(5)
    GP.output(red,False)

    GP.output(yellow,True)
    sleep(3)
    GP.output(yellow,False)

    GP.output(green,True)
    sleep(5)
    GP.output(green,False)

GP.cleanup()
