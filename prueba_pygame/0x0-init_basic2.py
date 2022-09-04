import pygame
import sys

#inicializr pygame
pygame.init()

#crear una  ventana Type: tupla
size = (800, 500)
screen = pygame.display.set_mode(size)

#bucle infinite
start = False
while not start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start= True
