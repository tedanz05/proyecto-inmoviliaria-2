import pygame
from settings import IMAGES_DIR

class PowerUp:
    def __init__(self, x, y):
        self.imagen = pygame.image.load(f"{IMAGES_DIR}/powerup.png").convert_alpha()
        self.rect = self.imagen.get_rect(center=(x,y))

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
