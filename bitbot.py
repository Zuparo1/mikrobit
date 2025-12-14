from microbit import *
import utime

# ----- PIN-OPPSETT -----
SONAR = pin15

LEFT_FWD = pin16
LEFT_REV = pin8
RIGHT_FWD = pin14
RIGHT_REV = pin12

# ----- ULTRALYD: MÅL AVSTAND -----
def get_distance_cm():
    # Send 10µs trigger-puls
    SONAR.write_digital(0)
    utime.sleep_us(2)
    SONAR.write_digital(1)
    utime.sleep_us(10)
    SONAR.write_digital(0)

    # Vent på at ekko-pulsen starter (pin går høy)
    start_wait = utime.ticks_us()
    while SONAR.read_digital() == 0:
        if utime.ticks_diff(utime.ticks_us(), start_wait) > 10000:  # 10 ms
            return 999  # timeout

    start = utime.ticks_us()

    # Vent på at ekko-pulsen slutter (pin går lav)
    while SONAR.read_digital() == 1:
        if utime.ticks_diff(utime.ticks_us(), start) > 20000:  # 20 ms
            return 999  # timeout

    end = utime.ticks_us()

    duration = utime.ticks_diff(end, start)
    distance_cm = duration / 58.0
    return distance_cm

# ----- MOTORFUNKSJONER -----
def forward():
    LEFT_FWD.write_digital(1)
    LEFT_REV.write_digital(0)
    RIGHT_FWD.write_digital(1)
    RIGHT_REV.write_digital(0)

def reverse():
    LEFT_FWD.write_digital(0)
    LEFT_REV.write_digital(1)
    RIGHT_FWD.write_digital(0)
    RIGHT_REV.write_digital(1)

def stop():
    LEFT_FWD.write_digital(0)
    LEFT_REV.write_digital(0)
    RIGHT_FWD.write_digital(0)
    RIGHT_REV.write_digital(0)

def turn_right():
    LEFT_FWD.write_digital(1)
    LEFT_REV.write_digital(0)
    RIGHT_FWD.write_digital(0)
    RIGHT_REV.write_digital(1)

# ----- HOVEDLØKKE -----
while True:
    d = get_distance_cm()

    if d < 20:
        display.show(Image.SAD)
    else:
        display.show(Image.HAPPY)


    if d < 20:
        stop()
        sleep(100)

        reverse()
        sleep(250)

        turn_right()
        sleep(250)

        stop()
        sleep(100)
    else:
        forward()

    sleep(20)
