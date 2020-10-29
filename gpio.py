import RPi.GPIO as GPIO


class Gpio:

    def __init__(self, button, light1, light2=None, light3=None):
        GPIO.setmode(GPIO.BCM)
        self.button = button
        setup_input(button)
        self.light1 = light1
        setup_output(light1, "LOW")
        self.light2 = light2
        if self.light2 is not None:
            setup_output(light2, "HIGH")
        self.light3 = light3
        if self.light3 is not None:
            setup_output(light3, "LOW")


def setup_input(pin):
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def setup_output(pin, start):
    GPIO.setup(pin, GPIO.OUT)
    if start == "HIGH":
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)


def set_output(pin, level):
    if level == "HIGH":
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)


def read_input(pin):
    return GPIO.input(pin)