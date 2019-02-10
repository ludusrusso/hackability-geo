import glob
from gpiozero import LED, Button
import pygame
from time import sleep

class Place(object):
    def __init__(self, mixer, folder, btn, stop_btn = None):
        self.mixer = mixer
        self.files = glob.glob('{}/*.mp3'.format(folder))
        self.index = 0

        self.btn = Button(btn)
        self.btn.when_pressed = self.play_next


    def _next(self):
        self.index = (self.index + 1) % len(self.files)

    def play(self):
        self.stop()
        sleep(1)
        self.mixer.music.load(self.files[self.index])
        self.mixer.music.play()

    def stop(self):
        self.mixer.music.stop()

    def play_next(self):
        self._next()
        self.play()
