from time import sleep

import gpio


def turn_on(pin):
    gpio.set_output(pin, "HIGH")


def turn_off(pin):
    gpio.set_output(pin, "LOW")


def strobe(pin, number, speed):
    for _ in range(number):
        turn_on(pin)
        sleep(speed)
        turn_off(pin)
        sleep(speed)