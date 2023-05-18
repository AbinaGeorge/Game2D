import pygame
from settings import *
from tiles import Tiles

class Level:
    
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface()
        
        self.visible_sprite = pygame.sprite.Group()
        self.obstacle_sprite = pygame.sprite.Group()
        self.create_world()
        
    def create_world(self):
        
        for row_index, row in enumerate(WORLDMAP):
            for col_index, col in enumerate(row):
                
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                
                if col == '*':
                    Tiles((x,y), self.visible_sprite)