import pygame
from settings import *

class Tiles(pygame.sprite.Sprite):
    
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.image.fill("green")