import pygame
import sys
from pathlib import Path
from personaje import Personaje
from explosion import Explosion
from enemigo import Enemigo
import random

from constantes import SCREEN_WIDTH, SCREEN_HEIGHT, START_IMAGE_PATH, IMPERIAL_MARCH_PATH, ESTRELLA_PATH, FONDO00_PATH

# Definir las rutas
ASSETS_PATH = "assets"

def mostrar_pantalla_inicio(screen):
    # cargar y mostrar la imagen del inicio
    imagen_inicio = pygame.image.load(START_IMAGE_PATH)
    imagen_inicio = pygame.transform.scale(imagen_inicio, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(imagen_inicio, (0, 0))
    pygame.display.flip()

   # reporducir audio
    pygame.mixer.music.load(IMPERIAL_MARCH_PATH)
    pygame.mixer.music.play()

    # esperar a que termine el audio
    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.event.post(event)
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
    sonido_explosion = pygame.mixer.Sound(f"{ASSETS_PATH}/sounds/explosion.mp3")

    personaje = Personaje(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    enemigos = []
    enemigos.append(Enemigo())  # Asegúrate de importar y crear la clase Enemigo
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

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx -= 5
        if keys[pygame.K_RIGHT]:
            dx += 5
        if keys[pygame.K_UP]:
            dy -= 5
        if keys[pygame.K_DOWN]:
            dy += 5
        personaje.mover(dx, dy)

        if keys[pygame.K_SPACE]:
            personaje.lanzar_laser()
            sonido_laser.play()

        for enemigo in enemigos[:]:
            enemigo.mover()
            if enemigo.rect.top > SCREEN_HEIGHT:
                enemigos.remove(enemigo)
                continue
                
            for laser in personaje.lasers[:]:
                if enemigo.rect.colliderect(laser.rect):
                    explosiones.append(Explosion(laser.rect.centerx, laser.rect.centery))
                    enemigos.remove(enemigo)
                    personaje.lasers.remove(laser)
                    sonido_explosion.play()
                    puntos += 10
                    break
                    
            if enemigo.rect.colliderect(personaje.rect):
                if not personaje.recibir_danio():
                    running = False
        
        if random.random() < 0.02:
            x = random.randint(0, SCREEN_WIDTH - 50)
            enemigos.append(Enemigo(x, 0))
            
        explosiones = [explosion for explosion in explosiones if explosion.actualizar()]
        
        screen.blit(fondo_actual, (0, 0))
        personaje.dibujar(screen)
        for enemigo in enemigos:
            enemigo.dibujar(screen)
        for explosion in explosiones:
            explosion.dibujar(screen)
            
        font = pygame.font.Font(None, 36)
        texto_puntos = font.render(f"Puntos: {puntos}", True, (255, 255, 255))
        texto_nivel = font.render(f"Nivel: {nivel}", True, (255, 255, 255))
        screen.blit(texto_puntos, (10, 50))
        screen.blit(texto_nivel, (10, 90))
        
        pygame.display.flip()
    
    screen.fill((0, 0, 0))
    texto_game_over = font.render("Game Over", True, (255, 255, 255))
    texto_mensaje_final = font.render("Que la fuerza te acompañe", True, (255, 255, 255))
    screen.blit(texto_game_over, (SCREEN_WIDTH // 2 - texto_game_over.get_width() // 2, SCREEN_HEIGHT // 2 - texto_game_over.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

