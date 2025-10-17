import pygame
from enemigo import Enemigo
from boxhead_game.powerup import PowerUp

class Nivel:
    def __init__(self):
        self.enemigos = []
        self.oleada = 1
        self.tiempo_spawn = 0
        self.powerups = []
        self.tiempo_powerup = 0

    def update(self, jugador):
        # Spawn enemigos
        self.tiempo_spawn += 1
        spawn_rate = max(40 - self.oleada*2, 10)
        if self.tiempo_spawn >= spawn_rate:
            self.enemigos.append(Enemigo())
            self.tiempo_spawn = 0

        # Spawn power-ups
        self.tiempo_powerup +=1
        if self.tiempo_powerup >= 600:
            self.powerups.append(PowerUp())
            self.tiempo_powerup = 0

        # Mover enemigos
        for enemigo in self.enemigos:
            enemigo.mover_hacia(jugador.rect)

        # Colisiones proyectiles
        for enemigo in self.enemigos[:]:
            for p in jugador.proyectiles[:]:
                if enemigo.rect.colliderect(p.rect):
                    if enemigo.recibir_golpe(10):
                        self.enemigos.remove(enemigo)
                    jugador.proyectiles.remove(p)
                    break

        # Colisiones jugador con power-ups
        for pu in self.powerups[:]:
            if jugador.rect.colliderect(pu.rect):
                pu.aplicar(jugador)
                self.powerups.remove(pu)

        # Aumentar oleada si no hay enemigos
        if len(self.enemigos)==0:
            self.oleada +=1

    def dibujar(self, pantalla):
        for enemigo in self.enemigos:
            enemigo.dibujar(pantalla)
        for pu in self.powerups:
            pu.dibujar(pantalla)
