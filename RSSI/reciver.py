from microbit import *
import radio

radio.on()
radio.config(channel=7)

MIN_RSSI = -100
MAX_RSSI = -40

def rssi_to_level(rssi):
    # Clamp to expected range
    if rssi < MIN_RSSI:
        rssi = MIN_RSSI
    if rssi > MAX_RSSI:
        rssi = MAX_RSSI

    span = MAX_RSSI - MIN_RSSI
    # Scale to 0–5
    level = int((rssi - MIN_RSSI) * 5 // span)
    return level

def show_bar(level):
    display.clear()
    x = 2  # middle column
    # level 0–5 lights from bottom→top
    for i in range(level):
        y = 4 - i  # bottom = y=4
        display.set_pixel(x, y, 9)

while True:
    packet = radio.receive_full()

    if packet:
        data, rssi, timestamp = packet
        level = rssi_to_level(rssi)
        show_bar(level)
    else:
        # No signal → small dot in the center
        display.set_pixel(2, 2, 5)
        sleep(100)
