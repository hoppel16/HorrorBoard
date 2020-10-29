from pygame import mixer


def load_sound(file_name):
    return mixer.music.load(file_name)


def play_sound():
    mixer.music.play()


def init():
    mixer.init()


def is_busy():
    return mixer.music.get_busy()
