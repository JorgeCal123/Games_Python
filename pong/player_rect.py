import pygame


class Player_rect:

    def __init__(self, screen, color, posicion, tamaño):
        self.player = pygame.draw.rect(screen, color, (posicion[0], posicion[1] -45, tamaño[0], tamaño[1]))

    def getPlayer(self):
        return self.player

