import sys
import RPi.GPIO as GPIO
import time
channel = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)
def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)
def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)
def get_temp(dev_file):
    f = open(dev_file,"r")
    contents = f.readlines()
    f.close()
    index = contents[-1].find("t=")
    if index != -1 :
        temperature = contents[-1][index+2:]
        cels =float(temperature)/1000
        return cels

temp = get_temp("/sys/bus/w1/devices/28-3c01a816dc0b/w1_slave")

while temp>10:
    if temp > 23.5:
        motor_on(channel)
        time.sleep(60)
        temp = get_temp("/sys/bus/w1/devices/28-3c01a816dc0b/w1_slave")
        GPIO.cleanup()
    else:
        motor_off(channel)
        time.sleep(60)
        temp = get_temp("/sys/bus/w1/devices/28-3c01a816dc0b/w1_slave")
        GPIO.cleanup()
