import pygame
import sys

"""
    REBOTE DE UN CUADRADO
"""

#inicializr pygame
pygame.init()

#crear una  ventana Type: tupla
size = (800, 500)
screen = pygame.display.set_mode(size)


#Lista de colores
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)   
GREEN = (0,255,0)
BLUE = (0,0,255)
# posicion del cuadrado
x= 400
y = 240
# velocidad del cuadrado
speed_x = 3
speed_y = 3
# timer del cuadrado
sleep = pygame.time.Clock()


#bucle infinite
while True:

    for event in pygame.event.get():
        """cerrar una ventana"""
        if event.type == pygame.QUIT:
            sys.exit()

    #color de fondo
    screen.fill(WHITE)

    if x > 720 or x < 0:
        speed_x *= -1
    if y > 320 or y< 0:
        speed_y *= -1

    x += speed_x
    y += speed_y
    pygame.draw.rect(screen, BLUE,(x, y, 50,50))

    #actualizar pantalla
    pygame.display.flip()
    sleep.tick(60)

    """
    ESTRUCTURA
        Logica
        Pantalla
        Digujo
        timer
    """