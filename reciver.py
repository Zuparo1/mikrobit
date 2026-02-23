from microbit import *
import radio

radio.on()
radio.config(channel=7)

# Definerer minimum og maksimum RSSI-verdi (signalstyrke)
MIN_RSSI = -100
MAX_RSSI = -40

# Funksjon som konverterer RSSI-verdi til et nivå fra 0 til 5
def rssi_to_level(rssi):
    if rssi < MIN_RSSI:
        rssi = MIN_RSSI
    if rssi > MAX_RSSI:
        rssi = MAX_RSSI

    span = MAX_RSSI - MIN_RSSI
    level = int((rssi - MIN_RSSI) * 5 // span)
    return level

# Funksjon som viser signalnivå som en vertikal stolpe på displayet
def show_bar(level):
    display.clear()
    x = 2
    for i in range(level):
        y = 4 - i  # bottom = y=4
        display.set_pixel(x, y, 9)

# Hovedløkke som kjører hele tiden
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
