import os
import gpio
import sound
import trigger
from pygame import mixer


# Raspberry Pi pin setup
button_pin = 16
light1_pin = 26
light2_pin = 6
light3_pin = 5
led1_pin = 17
led2_pin = 27
led3_pin = 22
led4_pin = 23
fog_on_pin = 24
fog_off_pin = 25
board = gpio.Gpio(button_pin, light1_pin, light2_pin, light3_pin, led1_pin, led2_pin, led3_pin, led4_pin, fog_on_pin, fog_off_pin)

# Initialize audio library
os_path = os.path.dirname(os.path.realpath(__file__)) + "/Sounds/"
file_name = "othermother_one_final.mp3"
file = os_path + file_name

sound.init(sound.get_sample_rate(file))

# Choose which trigger for this board
my_trigger = trigger.Trigger1(board, file)

try:
    while True:
        if not gpio.read_input(board.button) and not my_trigger.playing and not sound.is_busy():
            my_trigger.play()

finally:
    GPIO.cleanup()
    print("Have A Nice Day!")
