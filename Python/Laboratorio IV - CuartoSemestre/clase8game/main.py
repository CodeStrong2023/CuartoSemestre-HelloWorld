import pygame
import sys
from pathlib import Path

from constantes import SCREEN_WIDTH, SCREEN_HEIGHT, START_IMAGE_PATH, IMPERIAL_MARCH_PATH, ESTRELLA_PATH, FONDO00_PATH

# Definir las rutas
ASSETS_PATH = Path("assets")

def mostrar_pantalla_inicio(screen):
    # cargar y mostrar la imagen del inicio
    imagen_inicio = pygame.image.load(START_IMAGE_PATH)
    imagen_inicio = pygmae.trasnform.scale(imagen_inicio, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(imagen_inicio, (0, 0))
    pygame.display.flip()

   # reporducir audio
    pygame.mixer.music.load(IMPERIAL_MARCH_PATH)
    pygame.mixer.music.play()

    # esperar a que termine el audio
    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    #actualizar pantalla
    screen.blit(imagen_inicio, (0, 0))
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Amenaza Fantasma")

    
    # cargar los recursos del juego
    icon = pygame.image.load(ASSETS_PATH / "images/fondo00.png")
    pygame.display.set_icon(icon)

    fondo = pygame.image.load(f"{ASSETS_PATH}/images/fondo02.png")
    fondo = pygame.transform.scale(fondo, (SCREEN_WIDTH, SCREEN_HEIGHT))

    estrella = pygame.image.load(ESTRELLA_PATH)
    estrella = pygame.transform.scale(estrella, (SCREEN_WIDTH, SCREEN_HEIGHT))

    fondo = pygame.image.load(ASSETS_PATH / "images/fondo00.png")
    fondo = pygame.transform.scale(fondo, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    sonido_laser = pygame.mixer.Sound(f"{ASSETS_PATH}/sounds/laser.mp3")

    personaje = Personaje(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    enemigos = []
    explosiones = []
    puntos = 0
    nivel = 1

    clock = pygame.time.Clock()
    running = True

    # inicializar el fondo actual
    fondo_actual = fondo

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
