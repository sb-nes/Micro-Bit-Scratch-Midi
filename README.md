# Micro:bit Scratch Midi Controller
Trying to implement the functionality of Scratch DJing onto BBC's micro:bit microcontroller

## How to scratch (the very basics)
A Scratch Dj has one of his hands on the Jog Wheels and the other one on the crossfader/channel balance of the mixer.

While Scratching, the crossfader's curve is setup such that it works like an on/off switch. Therefore, it can easily be replaced by a capacitive touch button, or even a simple button (light, easy to press).

[Pending Implementation]


A simple Jog Wheel is a rotary encoder [we're gonna avoid motorized/belt driven Jog Wheels].
The distance travelled can be calculated from the accelerometer:
1. Check if the x/y axis of the accelerometer is above 'varying' threshold.
2. Add a constant displacement value to distance multiplied by a multiplier(currently only holds sign).
3. Return distance/displacement as midi.
4. Loop the algorithm every 'n' milliseconds.
[Note: the conversion is an approximation]

[without any multiplier, it feels more like scrubbing. Scratching is, in fact, scrubbing with emotion. Sorry!]

## Basics of MIDI:
Midi Signal [Around 3 bytes in length] = Status Byte (1 byte) + Pitch Byte (1 byte) + Data Byte (1 byte)
Data Rate = 31,250 bits/s

## Current Approach:

The MakeCode's Midi library: (compiled in C or C++)
It takes input in Binary or Hexadecimal
Raw Serial: It converts them into ASCII characters and sends them through the usb serial protocol. 

[ simple ver. it uses serial.print(convertToChar(0xA0)); or serial.print(convertToChar(1010 0001)); ]

Hairless Midi to Serial Bridge: It reads the serial comm. port, converts the data into ??? and sends it to the virtual midi channel [here, Loop Midi]
Loop Midi: Virtual Midi Channel, which is recognized by any DAW [Ableton, Studio One, FL Studio, Reaper, GarageBand, ProTools, etc.] or even Dj and Vj Software.

## Alternate Approaches:
1. Using an external 5-Din Midi Interface -> My audio interface supports 5-din midi connections.
2. Over Bluetooth -> Micro:bit currently only supports IOS. We'll have to wait for this one.

# References:
[To learn more about MIDI](https://midi.org/spec-detail)
[MIDI CC List](https://anotherproducer.com/online-tools-for-musicians/midi-cc-list/#)
[MIDI for DJ](https://github.com/mixxxdj/mixxx/wiki/MIDI-Crash-Course)
