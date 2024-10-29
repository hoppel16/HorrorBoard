import os
from mutagen.mp3 import MP3
from pygame import mixer


def setUpBoardWithSound(soundFile):
    self.sound = os.path.dirname(os.path.realpath(__file__)) + soundFile
    print("Setting up " + self.sound)
    self.board = board
    self.playing = False
    sound.load_sound(self.sound)


def init(sample_rate = 48000):
    mixer.init(frequency=sample_rate)


def load_sound(file_name):
    return mixer.music.load(file_name)


def play_sound():
    mixer.music.play()


def is_busy():
    return mixer.music.get_busy()


def get_sample_rate(file):
    mp3 = MP3(file)
    return mp3.info.sample_rate

