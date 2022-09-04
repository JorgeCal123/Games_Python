from turtle import Screen
import pygame
import sys

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

#bucle infinite
while True:

    for event in pygame.event.get():
        """cerrar una ventana"""
        if event.type == pygame.QUIT:
            sys.exit()

    #color de fondo
    screen.fill(WHITE)

    #dibujar figuras
    pygame.draw.line(screen, GREEN, [0,100], [100,100], 5)
    pygame.draw.circle(screen, BLUE, (100,100), 30)


    # Dibujar varias figuras al mismo tiempo
    # en el range son los pixeles de la figura 100 es donde inicia hasta 700
    # y los voy recorriendo cada 100 px
    for i in range(100,700, 100):
        pygame.draw.rect(screen, BLACK,(i, 230, 50,50))
        pygame.draw.line(screen, GREEN, [i,0], [i,100], 5)

    #actualizar pantalla
    pygame.display.flip()