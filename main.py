import pygame
from place import Place
import json
from gpiozero import Button
from time import sleep
from os import system

pygame.init()
pygame.mixer.init()

def set_volume(vol):
    system("amixer set PCM {}%".format(vol))

with open('geo.json') as f:
    data = json.load(f)

places = []
for place in data['folders']:
    p = Place(pygame.mixer, place['name'], place['button'])
    places.append(p)

btn = Button(data['stop'])
btn.when_pressed = places[0].stop

vol = data['volume']
set_volume(vol)


while True:
    sleep(10)
