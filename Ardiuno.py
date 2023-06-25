import pyfirmata
import time
from pyfirmata import *
from time import sleep

port = ''
pin = ''
board = pyfirmata.Arduino('')
theta0 = 90 
theta1 = 90
theta2 = 90
theta3 = 0  #for original posing of the servo
 
servo1 = board.get_pin('d:3:s')
servo2 = board.get_pin('d:5:s')
servo3 = board.get_pin('d:6:s')
servo4 = board.get_pin('d:9:s') 
trigpin = 11
ecopin = 12

#for servo1(base motor) 
def base(pin , angle):
    board.servo_config(3, angle = theta0)

    servo1.write(theta0)
    sleep(0.015)

def baseorg(pin , angle):
    board.servo_config(3, angle = theta3)

    servo1.write(theta3)
    sleep(0.015)

def elbow(pin , angle):
    board.servo_config(5, angle = theta1)

    servo2.write(theta1)
    sleep(0.015)

def elboworg(pin, angle):
    board.servo_config(6, angle = theta3)

    servo3.write(theta0)
    sleep(0.015)

def wrist(pin , angle):
    board.servo_config(6, angle = theta2)

    servo3.write(theta2)
    sleep(0.015)

def wristorg(pin, angle):
    board.servo_config(6, angle = theta3)

    servo3.write(theta3)
    sleep(0.015)


def closehand(pin , angle):
    board.servo_config(9, angle = theta3)

    servo4.write(theta2)
    sleep(0.015)

def openhand(pin , angle):
    board.sevo_config(9, angle = theta3)
    
    servo4.write(theta3)

def execute():
    base()
    sleep(1)
    elbow()
    sleep(1)
    wrist()
    sleep(1)
    closehand()
 #for the ultra sonic sensor
board.set_pin_mode_sonar(ecopin,trigpin,execute)
if(True):
    sleep(0.5)
    execute()
else:
    board.shutdown()




