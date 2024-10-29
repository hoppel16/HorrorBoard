import RPi.GPIO as GPIO


class Gpio:

    def __init__(self, button, light1, light2=None, light3=None, led1=None, led2=None, led3=None, led4=None, fog_on=None, fog_off=None):
        GPIO.setmode(GPIO.BCM)
        self.button = button
        setup_input(button)
        self.light1 = light1
        setup_output(light1, "LOW")
        self.light2 = light2
        if self.light2 is not None:
            setup_output(light2, "LOW")
        self.light3 = light3
        if self.light3 is not None:
            setup_output(light3, "LOW")
        self.led1 = led1
        if self.led1 is not None:
            setup_output(led1, "LOW")
        self.led2 = led2
        if self.led2 is not None:
            setup_output(led2, "LOW")
        self.led3 = led3
        if self.led3 is not None:
            setup_output(led3, "LOW")
        self.led4 = led4
        if self.led4 is not None:
            setup_output(led4, "LOW")
        self.fog_on = fog_on
        if self.fog_on is not None:
            setup_output(fog_on, "LOW")
        self.fog_off = fog_off
        if self.fog_off is not None:
            setup_output(fog_off, "LOW")


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