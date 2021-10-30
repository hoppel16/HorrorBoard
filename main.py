import gpio
import sound
import trigger


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
sound.init()

# Choose which trigger for this board
my_trigger = trigger.Trigger2(board)

try:
    while True:
        if not gpio.read_input(board.button) and not my_trigger.playing and not sound.is_busy():
            my_trigger.play()

finally:
    GPIO.cleanup()
    print("Have A Nice Day!")
