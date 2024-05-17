# this was to test if i can use the accelerometer to trigger a snare
# written in MakeCode
serial.set_baud_rate(BaudRate.BAUD_RATE115200)
trig = False

def on_every_interval():
    global trig
    serial.write_string("" + String.from_char_code(144) + String.from_char_code(36) + String.from_char_code(90)) # Kick Goes Every Half a Second
    if input.acceleration(Dimension.X) > 100:
        serial.write_string("" + String.from_char_code(144) + String.from_char_code(38) + String.from_char_code(90)) 
        # Snare if Micro:bit is pushed with enough force to the Right -> Sometimes it also causes accidental triggers
        trig = True
        
    sleep(100)
    serial.write_string("" + String.from_char_code(128) + String.from_char_code(36) + String.from_char_code(90))
    if (trig):
        serial.write_string("" + String.from_char_code(128) + String.from_char_code(38) + String.from_char_code(90))
        trig = False
loops.every_interval(500, on_every_interval)

def on_forever():
    pass
basic.forever(on_forever)
