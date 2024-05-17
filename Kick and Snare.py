# this was to test if i can use the accelerometer to trigger a snare
serial.set_baud_rate(BaudRate.BAUD_RATE115200)

def on_every_interval():
    serial.write_string("" + String.from_char_code(144) + String.from_char_code(36) + String.from_char_code(90))
    if input.acceleration(Dimension.X) > 100:
        serial.write_string("" + String.from_char_code(144) + String.from_char_code(38) + String.from_char_code(90))
loops.every_interval(500, on_every_interval)

def on_forever():
    pass
basic.forever(on_forever)
