import pygame
from settings import IMAGES_DIR

class Enemigo:
    def __init__(self, x, y):
        self.imagen = pygame.image.load(f"{IMAGES_DIR}/enemigo.png").convert_alpha()
        self.rect = self.imagen.get_rect(center=(x,y))
        self.vel = 2
        self.vida = 10

    def mover_hacia(self, jugador_rect):
        if self.rect.x < jugador_rect.x: self.rect.x += self.vel
        if self.rect.x > jugador_rect.x: self.rect.x -= self.vel
        if self.rect.y < jugador_rect.y: self.rect.y += self.vel
        if self.rect.y > jugador_rect.y: self.rect.y -= self.vel

    def recibir_golpe(self, dano):
        self.vida -= dano
        return self.vida <= 0

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
