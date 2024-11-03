import pygame
import random

class Enemigo:
    def __init__(self):
        self.image = pygame.Surface((50, 50))  # Superficie temporal
        self.image.fill((255, 0, 0))  # Color rojo
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)  # Ajusta según SCREEN_WIDTH
        self.rect.y = -50
        self.velocidad = 3

    def mover(self):
        self.rect.y += self.velocidad 