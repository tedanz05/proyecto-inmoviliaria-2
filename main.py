import pygame
from settings import ANCHO, ALTO, FPS, IMAGES_DIR
from jugador import Jugador
from enemigo import Enemigo
from proyectil import Proyectil
from powerup import PowerUp
from ui import dibujar_vida, dibujar_puntos, dibujar_boton

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Boxhead Python")
reloj = pygame.time.Clock()

# Fondo
fondo = pygame.image.load(f"{IMAGES_DIR}/fondo.png").convert()

# Jugador y enemigos
jugador = Jugador(ANCHO//2, ALTO//2)
enemigos = [Enemigo(100,100), Enemigo(700,500)]
proyectiles = []
powerups = [PowerUp(400,300)]
puntos = 0
vida = 100

game_over = False

while True:
    reloj.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if not game_over:
        keys = pygame.key.get_pressed()
        jugador.mover(keys)
        jugador.actualizar_cooldown()

        # Disparar
        if keys[pygame.K_SPACE]:
            jugador.disparar((1,0))  # ejemplo, disparo a la derecha

        # Mover enemigos
        for e in enemigos:
            e.mover_hacia(jugador.rect)

        # Dibujar todo
        pantalla.blit(fondo, (0,0))
        jugador.dibujar(pantalla)
        for e in enemigos:
            e.dibujar(pantalla)
        for p in powerups:
            p.dibujar(pantalla)
        dibujar_vida(pantalla, vida)
        dibujar_puntos(pantalla, puntos)
    else:
        pantalla.fill((0,0,0))
        dibujar_boton(pantalla, "Reintentar", ANCHO//2-70, ALTO//2-25, 140, 50)

    pygame.display.flip()
