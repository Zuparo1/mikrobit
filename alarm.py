from microbit import *
import music

# PINNEBRUK:
# IR-sensor → P1
# ADKeypad → P2 (analog)
# Buzzer → P0
# Rød LED → P8 (alarm)
# Blå LED → P16 (system aktivert)

alarm_on = False

def update_leds():
    if alarm_on:
        pin16.write_digital(1)  # blå: system aktivert
    else:
        pin16.write_digital(0)
        pin8.write_digital(0)  # slukk rød alarm-LED

update_leds()

# Funksjon for å lese hvem knapp som er trykket på ADKeypad
def read_button():
    value = pin2.read_analog()

    if 100 < value < 350:
        return "K1"   # Aktiver alarm
    if 400 < value < 650:
        return "K2"   # Deaktiver alarm

    return None

while True:
    btn = read_button()

    if btn == "K1":
        alarm_on = True
        update_leds()
        sleep(250)

    if btn == "K2":
        alarm_on = False
        update_leds()
        sleep(250)

    # IR-sensor: 1 betyr hindring/refleksjon
    ir = pin1.read_digital()

    if alarm_on and ir == 1:
        pin8.write_digital(1)  # rød alarm-LED
        music.play(['C5:2'], pin=pin0)
        display.show(Image.SKULL)
    else:
        pin8.write_digital(0)
        display.show(Image.HAPPY)

    sleep(50)

