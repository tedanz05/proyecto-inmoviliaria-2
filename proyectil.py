import pygame
from settings import ROJO

class Proyectil:
    def __init__(self, x, y, direccion, spread=0):
        self.rect = pygame.Rect(x, y, 5, 5)
        self.color = ROJO
        self.vel = 15
        self.direccion = direccion
        self.spread = spread

    def mover(self):
        self.rect.x += self.vel * self.direccion[0]
        self.rect.y += self.vel * self.direccion[1]

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, self.rect)
