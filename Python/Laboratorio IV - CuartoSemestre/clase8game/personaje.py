import pygame

class Personaje:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)  # Rectángulo básico para colisiones
        self.lasers = []
    
    def mover(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def lanzar_laser(self):
        # Implementar lógica de laser aquí
        pass 