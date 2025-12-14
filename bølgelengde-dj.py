from microbit import *
import music

frequencies = [200, 350, 500, 700, 900]
blink_times = [600, 400, 250, 180, 120]

waves = [
    Image("00000:00000:00900:00000:00000"),
    Image("00000:00000:09090:00000:00000"),
    Image("00000:00000:90909:00000:00000"),
    Image("00000:90909:00000:90909:00000"),
    Image("90909:00000:90909:00000:90909"),
]

level = 2

def show_level():
    display.show(waves[level])
    if level <= 1:
        pin1.write_digital(1)
        pin2.write_digital(0)
    elif level >= 3:
        pin1.write_digital(0)
        pin2.write_digital(1)
    else:
        pin1.write_digital(1)
        pin2.write_digital(1)

show_level()

while True:
    knapp_lav = pin8.read_digital()
    knapp_hoy = pin12.read_digital()

    if knapp_lav == 1:
        level = max(0, level - 1)
        show_level()
        sleep(200)

    if knapp_hoy == 1:
        level = min(4, level + 1)
        show_level()
        sleep(200)

    freq = frequencies[level]
    blink = blink_times[level]

    music.pitch(freq, blink, pin=pin0)
    sleep(50)
