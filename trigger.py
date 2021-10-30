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
<<<<<<< Updated upstream
        self.sound = os.path.dirname(os.path.realpath(__file__)) + "/Winnie_Hellogoodbye.mp3"
=======
        file_name = "new_mary.mp3"
        self.sound = os_path + file_name
        self.board = board
        self.playing = False
        sound.load_sound(self.sound)
        
    def play(self):
        self.playing = True
        sound.play_sound()
        sleep(0.35)
        # Binx scare - relay 1
        lights.strobe(self.board.light1, 20, 0.02)
        lights.turn_off(self.board.light1)
        #Black Flame Candle - LED 1
        sleep(6.26)
        lights.turn_on(self.board.led1)
        #Floor Light - relay 2
        sleep(2.5)
        lights.turn_on(self.board.light2)
        #Candle 1 - LED 2
        sleep(1.8)
        lights.turn_on(self.board.led2)
        #Candle 2 - LED 3
        sleep(2)
        lights.turn_on(self.board.led3)
        #Candle 3 - LED 4
        sleep(1.4)
        lights.turn_on(self.board.led4)
        #Cauldron - is the fog machine
        sleep(0.8)
        lights.turn_on(self.board.led5)
        #Mary scare
        sleep(2.6)
        lights.strobe(self.board.light3, 25, 0.02)
        lights.turn_on(self.board.light3)
        #turn off fog machine and floor lights here
        lights.turn_off(self.board.led5)
        lights.turn_off(self.board.light2)
        sleep(1.3)
        lights.strobe(self.board.light3, 35, 0.02)
        lights.turn_on(self.board.light3)
        sleep(5)
        lights.turn_off(self.board.light3)
        sleep(15.5)
        #turn off all lights
        lights.turn_off(self.board.led1)
        lights.turn_off(self.board.led2)
        lights.turn_off(self.board.led3)
        lights.turn_off(self.board.led4)
        self.playing = False
        

# LED string, NOT DONE
class Trigger3:
    def __init__(self, board):
        file_name = "winnie_hellogoodbye_final.mp3"
        self.sound = os_path + file_name
>>>>>>> Stashed changes
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
        lights.turn_on(self.board.led1)
        lights.turn_on(self.board.light1)
        lights.turn_on(self.board.light2)
        lights.turn_on(self.board.light3)
        sleep(2)
        lights.turn_off(self.board.led1)
        lights.turn_off(self.board.light1)
        lights.turn_off(self.board.light2)
        lights.turn_off(self.board.light3)
        
        lights.strobe(self.board.led1, 10, 0.02)
        self.playing = False
