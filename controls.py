__author__ = 'Muin'
import RPi.GPIO as GPIO
from pins import *
import time

#SETUP PINS
def initpins():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)
    GPIO.output(led1, False)
    GPIO.output(led2, False)


#MOTOR CONTROL FUNCTIONS
def forward():
    GPIO.output(led1, True)

def reverse():
    GPIO.output(led2, True)

def sudoleft():
    GPIO.output(led1, True)
    GPIO.output(led2, True)

def stop_sudoleft():
    GPIO.output(led1, False)
    GPIO.output(led2, False)

def stop_forward():
    GPIO.output(led1, False)

def stop_reverse():
    GPIO.output(led2, False)



#measuring distance
def distance():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(10, GPIO.IN)
    GPIO.output(8, GPIO.LOW)

    time.sleep(0.15)

    GPIO.output(8, True)
    time.sleep(0.00001)
    GPIO.output(8, False)

    while GPIO.input(10) == 0:
        pass
    start_time = time.time()

    while GPIO.input(10) == 1:
        pass
    end_time = time.time()

    total_time = end_time - start_time
    distance = (total_time * 170.145) * 100

    return distance




#button mobile edition
def powerled():
    forward()
    time.sleep(0.08)
    stop_forward()