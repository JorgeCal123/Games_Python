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


x = 10
y = 10
speed_x = 0
speed_y = 0
# oculta el puntero del mouse 
pygame.mouse.set_visible(0)

#bucle infinite
while True:

    for event in pygame.event.get():
        """cerrar una ventana"""
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("entra left")
                speed_x = -3
            if event.key == pygame.K_RIGHT:
                speed_x = 3
            if event.key == pygame.K_UP:
                speed_y = -3
            if event.key == pygame.K_DOWN:
                speed_y = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_x = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_UP:
                speed_y = 0
            if event.key == pygame.K_DOWN:
                speed_y = 0

    x += speed_x
    y += speed_y
    #color de fondo

    screen.fill(WHITE)
    # Dibuja un cuadrado de acuerdo a la posicion del mouse
    pygame.draw.rect(screen, RED,(x, y, 50,50))

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