import gpio
import sound
import trigger


# Raspberry Pi pin setup
button_pin = 16
light1_pin = 26
board = gpio.Gpio(button_pin, light1_pin, None, None)

# Initialize audio library
sound.init()

# Choose which trigger for this board
my_trigger = trigger.Trigger1(board)

try:
    while True:
        if not gpio.read_input(board.button) and not my_trigger.playing and not sound.is_busy():
        # if gpio.read_input(board.button) == "f" and not my_trigger.playing and not sound.is_busy():
            my_trigger.play()

finally:
    # GPIO.cleanup()
    print("Have A Nice Day!")
