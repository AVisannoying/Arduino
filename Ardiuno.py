import pyfirmata
import time
from pyfirmata import *
from time import sleep

board = Arduino('COM3')
theta0 = 90 
theta1 = 90
theta2 = 90
theta3 = 0  
theta4 = 0
theta5 = 0
 
servo1 = board.get_pin('d:3:s')
servo2 = board.get_pin('d:5:s')
servo3 = board.get_pin('d:6:s')
servo4 = board.get_pin('d:9:s') 

#for servo1(base motor) 
def base1(pin , angle):
    board.servo_config(3, angle = theta0)

    servo1.write(theta0)
    sleep(0.015)

def base1(pin , angle):
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
 

execute()






