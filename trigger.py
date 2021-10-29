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
        

class Trigger2:
    def __init__(self, board):
        file_name = "Winnie_Glorious_Final.mp3"
        self.sound = os_path + file_name
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
        file_name = "Winnie_Glorious_Final.mp3"
        self.sound = os_path + file_name
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
        file_name = "Winnie_Glorious_Final.mp3"
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
