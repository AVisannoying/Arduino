import pyfirmata
import time
from pyfirmata import *
from time import sleep

port = ''
pin = ''
board = pyfirmata.Arduino('')
theta0 = 90.0; 
theta1 = 90.0
theta2 = 90.0
theta3 = 0.0
 
servo1 = None
servo2 = None
servo3 = None
servo4=None 
trigpin = 11
ecopin = 12

#for servo1(base motor) 
def base(pin , angle):
    board.servo_config(3, angle = theta0)
    servo1 = board.get_pin('d:3:s')
    servo1.write(theta0)
    sleep(0.015)

def elbow(pin , angle):
    board.servo_config(5, angle = theta1)
    servo1 = board.get_pin('d:5:s')
    servo1.write(theta1)
    sleep(0.015)

def wrist(pin , angle):
    board.servo_config(6, angle = theta2)
    servo1 = board.get_pin('d:6:s')
    servo1.write(theta2)
    sleep(0.015)

def hand(pin , angle):
    board.servo_config(9, angle = theta3)
    servo1 = board.get_pin('d:9:s')
    servo1.write(theta3)
    sleep(0.015)

def execute():
    base()
    sleep(1)
    elbow()
    sleep(1)
    wrist()
    sleep(1)
    hand()

board.set_pin_mode_sonar(ecopin,trigpin,execute)
if(True):
    sleep(0.5)
    execute()
else:
    board.shutdown()




