# This was to implement and test how a rotary encoder works!
# Written in Micro:bit Python Editor -> micro:python

# Imports go at the top
from microbit import *
import math

class dir(enumerate):
    LEFT = 0
    RIGHT = 1
    NOT_MOVING = 2

# Declaration of Variable Independance
CLK = 0
DT = 0
SET = 0
DIR = dir.NOT_MOVING
Ready = False

vel = 0x00
x = 2
y = 2

# Sign Here

# Initialize
uart.init(115200)
CLK = pin13.read_digital()
DT = pin15.read_digital()
SET = pin13.read_digital()

#machine.time_pulse_us(pin13, DT, timeout_us=-1)

# Midi Data Through Serial
# uart.write(chr(0xB0)+chr(0x60)+chr(0x7F)+"\n")

def clamp(val, lower, upper):
    return min(upper, max(lower, val))

def move_pixel(pos = dir.LEFT):
    if(pos == dir.RIGHT):
        global x,y
        x = x + (y*5)
        x += 1
        if(x>24): # wrap around
            x = 0
        y = int(x / 5)
        x = int(x - (y*5))
    else:
        global x,y
        x = x + (y*5)
        x -= 1
        if(x<0): # wrap around
            x = 24
        x = clamp(x, 0, 24)
        y = int(x / 5)
        x = int(x - (y*5))
        

def Rotate(d):
    global SET, Ready, vel
    if(Ready==True):
        Ready = False
        if d == dir.RIGHT:
            vel = clamp(vel + 0x01, 0, 127)
            move_pixel(dir.RIGHT)
            # uart.write("Right\n")
        else:
            vel = clamp(vel - 0x01, 0, 127)
            move_pixel()
            # uart.write("Left\n")
    return

# Code in a 'while True:' loop repeats forever
while True:
    display.set_pixel(x,y,9)
    CLK = pin0.read_digital()
    DT = pin1.read_digital()
    #display.scroll(str(CLK)+str(DT))
    if(CLK ^ DT):
        if(CLK ^ SET):
            DIR = dir.RIGHT
        else:
            DIR = dir.LEFT
        Rotate(DIR)
    else:
        if(SET ^ CLK or SET ^ DT):
            SET = CLK = DT
            DIR = dir.NOT_MOVING
            #uart.write("ROTATED")
            uart.write(chr(0x90)+chr(0x24)+chr(vel))
            sleep(30)
            uart.write(chr(0x80)+chr(0x24)+chr(0x7F))
        Ready = True
    sleep(5)
    display.clear()
