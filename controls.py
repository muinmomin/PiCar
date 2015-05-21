__author__ = 'Muin'
import RPi.GPIO as GPIO
from pins import *
import time

#SETUP PINS
def initpins():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)


#MOTOR CONTROL FUNCTIONS
def forward():
    initpins()
    GPIO.output(7, False)
    GPIO.output(11, True)
    GPIO.output(13, True)
    GPIO.output(15, False)

def reverse():
    initpins()
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, True)

def left():
    initpins()
    GPIO.output(7, True)
    GPIO.output(11, True)
    GPIO.output(13, True)
    GPIO.output(15, False)

def right():
    initpins()
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, True)

def stop_left():
    GPIO.cleanup()

def stop_right():
    GPIO.cleanup()

def stop_forward():
    GPIO.cleanup()

def stop_reverse():
    GPIO.cleanup()




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