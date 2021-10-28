import os
from pygame import mixer


def setUpBoardWithSound(soundFile):
    self.sound = os.path.dirname(os.path.realpath(__file__)) + soundFile
    print("Setting up " + self.sound)
    self.board = board
    self.playing = False
    sound.load_sound(self.sound)

def load_sound(file_name):
    return mixer.music.load(file_name)


def play_sound():
    mixer.music.play()


def init():
    mixer.init()


def is_busy():
    return mixer.music.get_busy()
