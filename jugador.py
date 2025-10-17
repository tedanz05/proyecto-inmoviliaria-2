import pygame
from settings import IMAGES_DIR, SONIDO_DISPARO, ARMAS

class Jugador:
    def __init__(self, x, y):
        self.imagen = pygame.image.load(f"{IMAGES_DIR}/jackfree.png").convert_alpha()
        self.rect = self.imagen.get_rect(center=(x,y))
        self.vel = 5
        self.arma_actual = "pistola"
        self.cooldown = 0
        self.proyectiles = []
        self.sonido_disparo = pygame.mixer.Sound(SONIDO_DISPARO)

    def mover(self, keys):
        if keys[pygame.K_a]: self.rect.x -= self.vel
        if keys[pygame.K_d]: self.rect.x += self.vel
        if keys[pygame.K_w]: self.rect.y -= self.vel
        if keys[pygame.K_s]: self.rect.y += self.vel

    def disparar(self, direccion):
        if self.cooldown == 0:
            self.sonido_disparo.play()
            datos_arma = ARMAS[self.arma_actual]
            balas = datos_arma.get("balas",1)
            spread = datos_arma.get("spread",0)
            for i in range(balas):
                self.proyectiles.append([self.rect.centerx, self.rect.centery, direccion, spread])
            self.cooldown = datos_arma["cooldown"]

    def actualizar_cooldown(self):
        if self.cooldown > 0:
            self.cooldown -= 1

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
