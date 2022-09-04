import pygame
import sys

#inicializr pygame
pygame.init()

#crear una  ventana Type: tupla
size = (800, 500)
screen = pygame.display.set_mode(size)

#bucle infinite
while True:

    for event in pygame.event.get():
        """cerrar una ventana"""
        if event.type == pygame.QUIT:
            sys.exit()