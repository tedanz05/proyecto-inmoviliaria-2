import pygame
from settings import BLANCO, BOTON

pygame.font.init()
fuente = pygame.font.SysFont("arial",30)

def dibujar_vida(pantalla, vida):
    texto = fuente.render(f"Vida: {vida}", True, BLANCO)
    pantalla.blit(texto, (10,10))

def dibujar_puntos(pantalla, puntos):
    texto = fuente.render(f"Puntos: {puntos}", True, BLANCO)
    pantalla.blit(texto, (10,50))

def dibujar_boton(pantalla, texto_str, x, y, ancho, alto):
    pygame.draw.rect(pantalla, BOTON, (x,y,ancho,alto))
    texto = fuente.render(texto_str, True, (0,0,0))
    pantalla.blit(texto, (x+10,y+10))
