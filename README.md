# Micro:bit Scratch Midi Controller
Trying to implement the functionality of Scratch DJing onto BBC's micro:bit microcontroller

# Basics of MIDI:
Midi Signal [Around 3 bytes in length] = Status Byte (1 byte) + Pitch Byte (1 byte) + Data Byte (1 byte)
Data Rate = 31,250 bits/s

# Current Approach:

The MakeCode's Midi library: (compiled in C or C++)
It takes input in Binary or Hexadecimal
Raw Serial: It converts them into ASCII characters and sends them through the usb serial protocol. 

[ simple ver. it uses serial.print(convertToChar(0xA0)); or serial.print(convertToChar(1010 0001)); ]

Hairless Midi to Serial Bridge: It reads the serial comm. port, converts the data into ??? and sends it to the virtual midi channel [here, Loop Midi]
Loop Midi: Virtual Midi Channel, which is recognized by any DAW [Ableton, Studio One, FL Studio, Reaper, GarageBand, ProTools, etc.] or even Dj and Vj Software.

# Alternate Approaches:
1. Using an external 5-Din Midi Interface -> My audio interface supports 5-din midi connections.
2. Over Bluetooth -> Micro:bit currently only supports IOS. We'll have to wait for this one.
