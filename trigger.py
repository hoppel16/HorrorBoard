import os
from time import sleep

import sound
import lights

os_path = os.path.dirname(os.path.realpath(__file__)) + "/Sounds/"


class Trigger1:

    def __init__(self, board):
        file_name = "winnie_glorious_final.mp3"
        self.sound = os_path + file_name
        self.board = board
        self.playing = False
        sound.load_sound(self.sound)

    def play(self):
        self.playing = True
        sound.play_sound()
        sleep(0.5)
        lights.strobe(self.board.light1, 1, 0.1)
        lights.turn_on(self.board.light1)
        sleep(8.0)
        lights.turn_off(self.board.light1)
        self.playing = False
        

#Black flame sequence, Not done
#Change lights to their proper relay, and LED pins
class Trigger2:
    def __init__(self, board):
        file_name = "mary_final.mp3"
        self.sound = os_path + file_name
        self.board = board
        self.playing = False
        sound.load_sound(self.sound)
        
    def play(self):
        self.playing = True
        sound.play_sound()
        sleep(0.7)
        # Binx scare - relay 1
        lights.strobe(self.board.light2, 20, 0.02)
        lights.turn_off(self.board.light2)
        #Black Flame Candle - LED 1
        sleep(7.8)
        lights.turn_on(self.board.light2)
        #Floor Light - relay 2
        sleep(2.5)
        lights.turn_on(self.board.light2)
        #Candle 1 - LED 2
        sleep(1)
        lights.turn_on(self.board.light2)
        #Candle 2 - LED 3
        sleep(2)
        lights.turn_on(self.board.light2)
        #Candle 3 - LED 4
        sleep(2)
        lights.turn_on(self.board.light2)
        #Cauldron - is the fog machine
        sleep(7.8)
        lights.turn_on(self.board.light2)
        #Mary scare
        sleep(2.3)
        lights.strobe(self.board.light2, 25, 0.02)
        lights.turn_on(self.board.light2)
        #turn off fog machine and floor lights here
        lights.turn_off(self.board.light2)
        lights.turn_off(self.board.light2)
        sleep(5)
        lights.turn_off(self.board.light2)
        sleep(30)
        #turn off all lights
        lights.turn_off(self.board.light2)
        lights.turn_off(self.board.light2)
        lights.turn_off(self.board.light2)
        lights.turn_off(self.board.light2)
        self.playing = False
        

# LED string, NOT DONE
class Trigger3:
    def __init__(self, board):
        file_name = "winnie_hellogoodbye_final.mp3"
        self.sound = os_path + file_name
        self.board = board
        self.playing = False
        sound.load_sound(self.sound)
        
    def play(self):
        self.playing = True
        sound.play_sound()
        sleep(3)
        lights.turn_on(self.board.light1)
        sleep(3)
        lights.turn_off(self.board.light1)
        self.playing = False
        

class Trigger4:
    def __init__(self, board):
        file_name = "sara_trick_final.mp3"
        self.sound = os_path + file_name
        self.board = board
        self.playing = False
        sound.load_sound(self.sound)
        
    def play(self):
        self.playing = True
        sound.play_sound()
        sleep(0.3)
        lights.strobe(self.board.light1, 5, 0.05)
        lights.turn_on(self.board.light1)
        sleep(0.75)
        lights.strobe(self.board.light1, 5, 0.05)
        lights.turn_off(self.board.light1)
        self.playing = False
        
        
class Trigger5:
    def __init__(self, board):
        file_name = "billy_final.mp3"
        self.sound = os_path + file_name
        self.board = board
        self.playing = False
        sound.load_sound(self.sound)
        
    def play(self):
        self.playing = True
        sound.play_sound()
        sleep(0.45)
        lights.strobe(self.board.light1, 9, 0.02)
        lights.turn_off(self.board.light1)
        sleep(0.28)
        lights.strobe(self.board.light1, 9, 0.02)
        lights.turn_on(self.board.light1)
        sleep(1.95)
        lights.strobe(self.board.light1, 2, 0.05)
        lights.turn_off(self.board.light1)
        sleep(0.55)
        lights.strobe(self.board.light1, 3, 0.05)
        lights.turn_off(self.board.light1)
        self.playing = False
        
        
class Trigger6:
    def __init__(self, board):
        file_name = "winnie_ugly_final.mp3"
        self.sound = os_path + file_name
        self.board = board
        self.playing = False
        sound.load_sound(self.sound)
        
    def play(self):
        self.playing = True
        sound.play_sound()
        sleep(0.3)
        lights.strobe(self.board.light1, 15, 0.05)
        lights.turn_on(self.board.light1)
        sleep(6.0)
        lights.turn_off(self.board.light1)
        self.playing = False
        
class TriggerTest:
    def __init__(self, board):
        file_name = "winnie_ugly_final.mp3"
        self.sound = os_path + file_name
        self.board = board
        self.playing = False
        sound.load_sound(self.sound)
        
    def play(self):
        self.playing = True
        sound.play_sound()
        lights.turn_on(self.board.light1)
        lights.turn_on(self.board.light2)
        lights.turn_on(self.board.light3)
        sleep(2)
        lights.turn_off(self.board.light1)
        lights.turn_off(self.board.light2)
        lights.turn_off(self.board.light3)
        self.playing = False
