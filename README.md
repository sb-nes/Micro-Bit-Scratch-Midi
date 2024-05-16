# Micro:bit Scratch Midi Controller
Trying to implement the functionality of Scratch DJing onto BBC's micro:bit microcontroller

# Basics of MIDI:
Midi Signal [Around 3 bytes in length] = Status Byte (1 byte) + Pitch Byte (1 byte) + Data Byte (1 byte)
Data Rate = 31,250 bits/s

# Current Approach:

The MakeCode's Midi library: (compiled in C or C++)
It takes input in Binary or Hexadecimal
Raw Serial: It converts them into ASCII characters and sends them through the usb serial protocol. 
[simple ver. it uses serial.print(convertToChar(0xA0)); or serial.print(convertToChar(1010 0001));

Hairless Midi to Serial Bridge:
Loop Midi:
