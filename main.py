import pygame
from place import Place
import json

pygame.init()
pygame.mixer.init()

with open('geo.json') as f:
    data = json.load(f)

places = []
for place in data['folders']:
    p = Place(pygame.mixer, place['name'], place['button'])
    places.append(p)

btn = Button(data['stop'])
btn.when_pressed = places[0].stop

while True:
    sleep(10)