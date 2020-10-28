import RPi.GPIO as GPIO
from time import sleep
from pygame import mixer

# Variable Definition
rly_pin = 26
btn_pin = 16
sound_file = "Alma TS.mp3"
isPlaying = False

# Set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(rly_pin, GPIO.OUT)
GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize pygame mixer and load sound
mixer.init()
music = mixer.music
music.load(sound_file)

# Function setup
def turnOnLight(sleepTime):
    GPIO.output(rly_pin, GPIO.HIGH)
    sleep(sleepTime)

def turnOffLight(sleepTime):
    GPIO.output(rly_pin, GPIO.LOW)
    sleep(sleepTime)
    
def strobe(amount, sleepTime):
    for _ in range(amount):
        turnOnLight(sleepTime)
        turnOffLight(sleepTime)

def trigger():
    music.play()
    sleep(0.5)
    strobe(6, 0.1)
    turnOnLight(2.6)
    turnOffLight(0.3)
    strobe(3, 0.05)

# Start board
try:
    while True:
        if not GPIO.input(btn_pin) and not isPlaying:
            isPlaying = True
            trigger()
            isPlaying = False

finally:
    GPIO.cleanup()
