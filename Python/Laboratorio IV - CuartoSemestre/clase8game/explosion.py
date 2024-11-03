import pygame
import os

from constantes import ASSETS_PATH
class Explosion:
    def __init__(self, x, y):
        self.imagenes = [pygame.image.load(os.path.join(ASSETS_PATH, f"images/explosion/{i:02d}.png")) for i in range(9)]
        self.index = 0
        self.rect = self.imagenes[0].get_rect(center=(x, y))
        self.frame_rate = 0
        self.max_frame_rate = 5

    def actualizar(self):
        self.frame_rate += 1
        if self.frame_rate >= self.max_frame_rate:
            self.frame_rate = 0
            self.index += 1
            if self.index >= len(self.imagenes):
                return False
        return True
    
    def dibujar(self, screen):
        screen.blit(self.imagenes[self.index], self.rect.topleft)