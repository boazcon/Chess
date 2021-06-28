# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:29:12 2021

@author: boaz cohen
"""
import pygame


BLACK=(0,0,0)
WHITE=(255,255,255)
FPS=60  
ROWS ,COLS=8,8
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
SQUARE_SIZE=WINDOW_WIDTH//COLS

                            


class ChessBoard:
    def __init__(self):
        self.board=[]
        self.selected_piece=None
        
        
    def GetPos(self):
        return self.board
    
    
    
    
    
    
    def draw_squres(self,win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row %2,COLS,2):
                pygame.draw.rect(win,WHITE,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
                self.board=[row,col]
                
            
                
    
                
                        
   
        


                    
                        
                
                    
                    
                    
                            
                
        
