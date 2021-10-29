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
