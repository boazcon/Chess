# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:45:43 2021

@author: user
"""
#from ViewBoard import BLACK ,WHITE, SQUARE_SIZE,PAWN
# import pieces
import pygame
BLACK=(0,0,0)
WHITE=(255,255,255)
FPS=60  
ROWS ,COLS=8,8
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
SQUARE_SIZE=WINDOW_WIDTH//COLS
PAWN=pygame.transform.scale(pygame.image.load(r'C:\Users\user\Desktop\Chess\pieces\bp.png'
), (44,25))
import pygame


class Pieces(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.PAWN = pygame.image.load(PAWN).convert()
        self.x = x
        self.y = y
        
    def update_loc(self, x, y):
        self.x = x
        self.y = y
   
    def get_pos(self):
        return self.x, self.y

    




    
    
    
    
    
    
    
    
                 