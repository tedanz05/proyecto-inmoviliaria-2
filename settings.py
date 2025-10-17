import os

# -------------------
# Configuración de ventana
# -------------------
ANCHO, ALTO = 800, 600
FPS = 60

# -------------------
# Colores
# -------------------
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (50, 150, 255)
AMARILLO = (255, 255, 0)
BOTON = (200, 200, 200)

# -------------------
# Directorios de assets
# -------------------
# Carpeta principal de assets
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

# Carpeta de imágenes
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")

# Carpeta de sonidos
SOUNDS_DIR = os.path.join(ASSETS_DIR, "sounds")

# -------------------
# Sonidos
# -------------------
SONIDO_DISPARO = os.path.join(SOUNDS_DIR, "disparo.wav")
SONIDO_EXPLOSION = os.path.join(SOUNDS_DIR, "explosion.wav")
SONIDO_POWERUP = os.path.join(SOUNDS_DIR, "powerup.wav")

# -------------------
# Armas del jugador
# -------------------
ARMAS = {
    "pistola": {"vel": 10, "balas": 1, "cooldown": 20},
    "uzi": {"vel": 15, "balas": 1, "cooldown": 5},
    "escopeta": {"vel": 12, "balas": 5, "spread": 15, "cooldown": 40}
}
