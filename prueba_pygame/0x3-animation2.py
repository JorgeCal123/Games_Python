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
# posicion del cuadrado
x= 400
y = 240
# velocidad del cuadrado
speed_x = 3
speed_y = 3
# timer del cuadrado

list_circle= []
#Dibujo 60 circulos
for i in range(60):
    x = random.randint(0,800)
    y = random.randint(0,500)
    list_circle.append([x,y])
 

#bucle infinite
while True:

    for event in pygame.event.get():
        """cerrar una ventana"""
        if event.type == pygame.QUIT:
            sys.exit()
    #color de fondo
    screen.fill(WHITE)
    for i in list_circle:
        x = i[0]
        y = i[1]
        pygame.draw.circle(screen, BLUE, (x,y), 10)
        i[1] += 1
        if i[1] > 500:
            i[1] = 0


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