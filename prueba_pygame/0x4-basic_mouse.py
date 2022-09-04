import pygame
import sys
import random
"""
    Simulacion de una Lluvia
"""

#inicializr pygame
pygame.init()

#crear una  ventana Type: tupla
size = (800, 500)
screen = pygame.display.set_mode(size)
sleep = pygame.time.Clock()


#Lista de colores
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)   
GREEN = (0,255,0)
BLUE = (0,0,255) 


# oculta el puntero del mouse 
pygame.mouse.set_visible(0)

#bucle infinite
while True:

    for event in pygame.event.get():
        """cerrar una ventana"""
        if event.type == pygame.QUIT:
            sys.exit()

    # tupla con la posicion del mouse en todo momento
    mousepos = pygame.mouse.get_pos()
    #color de fondo
    screen.fill(WHITE)
    # Dibuja un cuadrado de acuerdo a la posicion del mouse
    pygame.draw.rect(screen, RED,(mousepos[0], mousepos[1], 50,50))

    #actualizar pantalla
    pygame.display.flip()

    #SLEEP DE LA ANIMACION
    sleep.tick(60)

    """
    ESTRUCTURA
        Logica
        Pantalla
        Digujo
        timer
    """