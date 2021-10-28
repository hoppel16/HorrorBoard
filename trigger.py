import os
from time import sleep

import sound
import lights


class Trigger1:

    def __init__(self, board):
        self.sound = os.path.dirname(os.path.realpath(__file__)) + "/Winnie_Glorious_Morning.mp3"
        self.board = board
        self.playing = False
        sound.load_sound(self.sound)

    def play(self):
        self.playing = True
        sound.play_sound()
        lights.turn_on(self.board.light1)
        sleep(5.0)
        lights.turn_off(self.board.light1)
        self.playing = False
        

class Trigger2:
    def __init__(self, board):
        self.sound = os.path.dirname(os.path.realpath(__file__)) + "/Winnie_Hellogoodbye.mp3"
        self.board = board
        self.playing = False
        sound.load_sound(self.sound)
        
    def play(self):
        self.playing = True
        sound.play_sound()
        lights.strobe(self.board.light2, 30, 0.05)
        lights.turn_on(self.board.light1)
        sleep(5)
        lights.turn_off(self.board.light1)
        self.playing = False
        
        
class Trigger3:
    def __init__(self, board):
        self.sound = os.path.dirname(os.path.realpath(__file__)) + "/sara_trick_final.mp3"
        self.board = board
        self.playing = False
        sound.load_sound(self.sound)
        
    def play(self):
        self.playing = True
        sound.play_sound()
        lights.turn_on(self.board.light1)
        lights.turn_on(self.board.light2)
        lights.strobe(self.board.light3, 10, 0.25)
        sleep(4)
        lights.turn_off(self.board.light1)
        lights.turn_off(self.board.light2)
        self.playing = False
        
        
class TriggerTest:
    def __init__(self, board):
        self.sound = os.path.dirname(os.path.realpath(__file__)) + "/Sara_amok_one.mp3"
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
