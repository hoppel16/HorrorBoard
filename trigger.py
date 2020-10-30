import os
from time import sleep

import sound
import lights


class Trigger1:

    def __init__(self, board):
        self.sound = os.path.dirname(os.path.realpath(__file__)) + "/Alma_TS.mp3"
        self.board = board
        self.playing = False
        sound.load_sound(self.sound)

    def play(self):
        self.playing = True
        sound.play_sound()
        sleep(0.5)
        lights.strobe(self.board.light1, 6, 0.1)
        lights.turn_on(self.board.light1)
        sleep(2.6)
        lights.turn_off(self.board.light1)
        sleep(0.3)
        lights.strobe(self.board.light1, 3, 0.05)
        self.playing = False

class Trigger2:
    def __init__(self, board):
        self.sound = os.path.dirname(os.path.realpath(__file__)) + "/demon_trigger.mp3"
        self.board = board
        self.playing = False
        sound.load_sound(self.sound)
        
    def play(self):
        self.playing = True
        sound.play_sound()
        sleep(0.7)
        lights.strobe(self.board.light1, 30, 0.05)
        self.playing = False
        
class Trigger3:
    def __init__(self, board):
        self.sound = os.path.dirname(os.path.realpath(__file__)) + "/demon_trigger.mp3"
        self.board = board
        self.playing = False
        sound.load_sound(self.sound)
        
        lights.turn_on(self.board.light2)
        lights.turn_off(self.board.light1)
        
    def play(self):
        self.playing = True
        sound.play_sound()
        sleep(0.7)
        lights.turn_on(self.board.light1)
        lights.turn_off(self.board.light2)
        sleep(1)
        lights.turn_off(self.board.light1)
        lights.turn_on(self.board.light2)
        self.playing = False
        
class Trigger4:
    def __init__(self, board):
        self.sound = os.path.dirname(os.path.realpath(__file__)) + "/Alma_burning_TS.mp3"
        self.board = board
        self.playing = False
        sound.load_sound(self.sound)

    def play(self):
        self.playing = True
        sound.play_sound()
        sleep(0.5)
        lights.strobe(self.board.light1, 12, 0.1)
        lights.strobe(self.board.light1, 12, 0.2)
        lights.strobe(self.board.light1, 7, 0.3)
        lights.strobe(self.board.light1, 5, 0.4)
        lights.strobe(self.board.light1, 3, 0.5)
        self.playing = False
