# This was to implement and test how a rotary encoder works!
# Written in Micro:bit Python Editor -> micro:python
# Using Numark MIXTRACK MIDI mapping on MIXXX

# Imports go at the top
from microbit import *

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

val = 0x00
x = 2
y = 2

# Sign Here

# Initialize
uart.init(115200)
CLK = pin13.read_digital()
DT = pin15.read_digital()
SET = pin13.read_digital()

# Machine.time_pulse_us(pin13, DT, timeout_us=-1)

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
    global SET, Ready, vel, val
    if(Ready==True):
        Ready = False
        # the 
        if d == dir.RIGHT:
            val = 0x0F
            move_pixel(dir.RIGHT)
        else:
            val = 0x72
            move_pixel()
    return

# Code in a 'while True:' loop repeats forever
while True:
    display.set_pixel(x,y,9)
    CLK = pin0.read_digital()
    DT = pin1.read_digital()

    if button_a.is_pressed():
        uart.write(chr(0x90)+chr(0x42)+chr(0x7F))
        sleep(1000)
    if button_b.is_pressed():
        uart.write(chr(0x90)+chr(0x42)+chr(0x00))
    if pin2.is_touched():
        uart.write(chr(0x90)+chr(0x3C)+chr(0x7F))
    if pin_logo.is_touched():
        uart.write(chr(0x90)+chr(0x48)+chr(0x7F))
    
    #display.scroll(str(CLK)+str(DT))
    if(CLK ^ DT): # start rotate
        if(CLK ^ SET):
            DIR = dir.RIGHT
        else:
            DIR = dir.LEFT
        Rotate(DIR)
    else:
        if(SET ^ CLK or SET ^ DT): # end rotate
            SET = CLK = DT
            DIR = dir.NOT_MOVING
            uart.write(chr(0xB0)+chr(0x18)+chr(val)) # Deck 2
            display.clear()
        Ready = True
    #sleep(5)
