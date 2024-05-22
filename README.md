# Micro:bit Scratch Midi Controller
Trying to implement the functionality of Scratch DJing onto BBC's micro:bit microcontroller

## Hardware/Software Used
* BBC's Micro:Bit controller [Main]
* Rotary Encoder
* [Hairless MIDI](https://projectgus.github.io/hairless-midiserial/) [Converts Serial MIDI and bridges connection between serial/COM and the virtual driver]
* LoopMidi [For a Virtual Emulation of a Midi Adapter/Driver](https://www.tobias-erichsen.de/software/loopmidi.html)

## How to scratch (the very basics)
A Scratch Dj has one of his hands on the Jog Wheels and the other one on the crossfader/channel balance of the mixer.

While Scratching, the crossfader's curve is setup such that it works like an on/off switch. Therefore, it can easily be replaced by a capacitive touch button, or even a simple button (light, easy to press).

[Pending Implementation]


A simple Jog Wheel is a rotary encoder [we're gonna avoid motorized/belt driven Jog Wheels].

Status code -> 0xB0 [midi CC at midi channel 0] & Pitch code -> Assigned CC Channel #

### Data Value:
Left -> 0x01-0x3F

Right -> 0x41-0x7F


### Emulating Rotary Encoder using an Accelerometer:
1. Check if the x/y axis of the accelerometer is above 'varying' threshold.
2. Use a second threshold to distinguish between slow or fast movements.

[a slow movement means it is covering a short distance every tick, thus it fires exactly once]

[a fast movement means that it has covered a larger distance, thus needs to fire multiple times to achieve the same on the encoder]

3. return how many times the midi signals data.

[Note: the conversion is an approximation]

[without any multiplier, it feels more like scrubbing. Scratching is, in fact, scrubbing with emotion. Sorry!]

## Basics of MIDI
Midi Signal [Around 3 bytes in length] = Status Byte (1 byte) + Pitch Byte (1 byte) + Data Byte (1 byte)
Data Rate = 31,250 bits/s

## Current Approach
My code currently doesn't use Interrupts for Rotary Encoders.

The MakeCode's Midi library: (compiled in C or C++)
It takes input in Binary or Hexadecimal
Raw Serial: It converts them into ASCII characters and sends them through the usb serial protocol. 

[ simple ver. it uses serial.print(convertToChar(0xA0)); or serial.print(convertToChar(1010 0001)); ]

example for MIDI DATA: serial.print( chr(0x80)+chr(0x24)+chr(0x7F) ) -> Note On, Channel 0, Pitch = C1, Velocity = 127

Hairless Midi to Serial Bridge: It reads the serial comm. port, converts the data into ??? and sends it to the virtual midi channel [here, Loop Midi]
Loop Midi: Virtual Midi Channel, which is recognized by any DAW [Ableton, Studio One, FL Studio, Reaper, GarageBand, ProTools, etc.] or even Dj and Vj Software.

## Alternate Approaches
1. Using an external 5-Din Midi Interface -> My audio interface supports 5-din midi connections.
2. Over Bluetooth -> Micro:bit currently only supports IOS. We'll have to wait for this one.

# References:
[To learn more about MIDI](https://midi.org/spec-detail)

[A Little Theory to ride along](https://learn.sparkfun.com/tutorials/midi-tutorial/all)

[MIDI CC List](https://anotherproducer.com/online-tools-for-musicians/midi-cc-list/#)

[MIDI for DJ](https://github.com/mixxxdj/mixxx/wiki/MIDI-Crash-Course)
