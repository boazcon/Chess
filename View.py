# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:08:47 2021

@author: boaz cohen
"""
import pygame
from Chess import * 

from ViewBoard import ChessBoard 

FPS=12
ROWS ,COLS=8,8
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
SQUARE_SIZE=WINDOW_WIDTH//COLS

BLACK=(0,0,0)
WHITE=(255,255,255)

LEFT=1

Background=r'C:\Users\user\Desktop\projects\Chess\pieces\s8XND.png'
BlackPAWN=r'C:\Users\user\Desktop\projects\Chess\pieces\bp.png'
BlaclKnight=r'C:\Users\user\Desktop\projects\Chess\pieces\bN.png'
BlaclSteeple=r'C:\Users\user\Desktop\projects\Chess\pieces\bR.png'
BlacklQueen=r'C:\Users\user\Desktop\projects\Chess\pieces\bQ.png'
BlacklKing=r'C:\Users\user\Desktop\projects\Chess\pieces\bK.png'
BlackBishop=r'C:\Users\user\Desktop\projects\Chess\pieces\bB.png'



WhitePAWN=r'C:\Users\user\Desktop\projects\Chess\pieces\wp.png'
WhiteKnight=r'C:\Users\user\Desktop\projects\Chess\pieces\wN.png'
WhiteSteeple=r'C:\Users\user\Desktop\projects\Chess\pieces\wR.png'
WhiteQueen=r'C:\Users\user\Desktop\projects\Chess\pieces\wQ.png'
WhiteKing=r'C:\Users\user\Desktop\projects\Chess\pieces\wK.png'
WhiteBishop=r'C:\Users\user\Desktop\projects\Chess\pieces\wB.png'


def roundxy(x,y):
    x=int(x/100)
    y=int(y/100)

    return x,y
    
    
def conversion(x,y):
    x=x*100+20
    y=y*100+20
    return x,y



class ViewPlayers():
        def __init__(self,x,y):
            super(self.__class__,self).__init__()
            self.x=x
            self.y=y
            self.rect=self.image.get_rect()
            self.rect.x=x
            self.rect.y=y
            self.team=True
    
        
        def GetLoc(self):
            return self.x,self.y
        
        def GetTeam(self):
            return self.team
        
        def UpdateLoc(self,x,y):
            self.rect.x=x
            self.rect.y=y
            self.x=x
            self.y=y
            
            
            
            
class ViewQueenBlack(pygame.sprite.Sprite,ViewPlayers):
    
    
    def __init__(self,x,y):
        super(self.__class__,self).__init__()
        self.x=x
        self.y=y
        self.image=pygame.image.load(BlacklQueen).convert()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.team=False

      

class ViewPawnBlack(pygame.sprite.Sprite,ViewPlayers):
    
    
    def __init__(self,x,y):
        super(self.__class__,self).__init__()
        self.x=x
        self.y=y
        self.image=pygame.image.load(BlackPAWN).convert()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.team=False


        
        
        
        
class ViewSteepleBlack(pygame.sprite.Sprite,ViewPlayers):
    
    
    def __init__(self,x,y):
        super(self.__class__,self).__init__()
        self.x=x
        self.y=y
        self.image=pygame.image.load(BlaclSteeple).convert()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.team=False


            
class ViewKnightBlack(pygame.sprite.Sprite,ViewPlayers):
        
    def __init__(self,x,y):
        super(self.__class__,self).__init__()
        self.x=x
        self.y=y
        self.image=pygame.image.load(BlaclKnight).convert()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.team=False

        
    
    
        
class ViewKingBlack(pygame.sprite.Sprite,ViewPlayers):
    
    
    def __init__(self,x,y):
        super(self.__class__,self).__init__()
        self.x=x
        self.y=y
        self.image=pygame.image.load(BlacklKing).convert()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.team=False


    
class ViewBishopBlack(pygame.sprite.Sprite,ViewPlayers):
    
    
    def __init__(self,x,y):
        super(self.__class__,self).__init__()
        self.x=x
        self.y=y
        self.image=pygame.image.load(BlackBishop).convert()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.team=False


    
    #white players
    
class ViewQueenWhite(pygame.sprite.Sprite,ViewPlayers):
    
    
    def __init__(self,x,y):
        super(self.__class__,self).__init__()
        self.x=x
        self.y=y
        self.image=pygame.image.load(WhiteQueen).convert()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.team=True

      

class ViewPawnWhite(pygame.sprite.Sprite,ViewPlayers):
    
    
    def __init__(self,x,y):
        super(self.__class__,self).__init__()
        self.x=x
        self.y=y
        self.image=pygame.image.load(WhitePAWN).convert()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.team=True


        
        
        
        
class ViewSteepleWhite(pygame.sprite.Sprite,ViewPlayers):
    
    
    def __init__(self,x,y):
        super(self.__class__,self).__init__()
        self.x=x
        self.y=y
        self.image=pygame.image.load(WhiteSteeple).convert()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.team=True


        
class ViewKnightWhite(pygame.sprite.Sprite,ViewPlayers):
    
    
    def __init__(self,x,y):
        super(self.__class__,self).__init__()
        self.x=x
        self.y=y
        self.image=pygame.image.load(WhiteKnight).convert()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.team=True

        
class ViewKingWhite(pygame.sprite.Sprite,ViewPlayers):
    
    
    def __init__(self,x,y):
        super(self.__class__,self).__init__()
        self.x=x
        self.y=y
        self.image=pygame.image.load(WhiteKing).convert()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.team=True

 
    
class ViewBishopWhite(pygame.sprite.Sprite,ViewPlayers):
    
    
    def __init__(self,x,y):
        super(self.__class__,self).__init__()
        self.x=x
        self.y=y
        self.image=pygame.image.load(WhiteBishop).convert()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.team=True


    

    
#TODO  להעביר את הcontroller למקום אחר.

def main():
    
    board=Board()
    pygame.init()
    WIN=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT)) 
    pygame.display.set_caption("Game")
    
    BoardChess=ChessBoard()
    Pos_From_To=[]
    AllPlayerlist=pygame.sprite.Group() 
    WhitePlayerlist=pygame.sprite.Group() 
    BlackPlayerlist=pygame.sprite.Group() 

    
    #whites players: pawn

    for i in range(20,800,100):
            WhitePawn=ViewPawnWhite(i,620)
            AllPlayerlist.add(WhitePawn)
            WhitePlayerlist.add(WhitePawn)

    #add the White Knight to the board

    WhiteKnight=ViewKnightWhite(120,720)
    AllPlayerlist.add(WhiteKnight) 
    WhitePlayerlist.add(WhiteKnight) 
    WhiteKnight=ViewKnightWhite(620,720)
    AllPlayerlist.add(WhiteKnight) 
    WhitePlayerlist.add(WhiteKnight) 
    
    #add the White Steeple to the board

    
    WhiteSteeple=ViewSteepleWhite(20,720)
    AllPlayerlist.add(WhiteSteeple) 
    WhitePlayerlist.add(WhiteSteeple) 

    WhiteSteeple=ViewSteepleWhite(720,720)
    AllPlayerlist.add(WhiteSteeple)
    WhitePlayerlist.add(WhiteSteeple) 


#add bishop White




    WhiteBishop=ViewBishopWhite(220,720)
    AllPlayerlist.add(WhiteBishop) 
    WhitePlayerlist.add(WhiteBishop) 

    WhiteBishop=ViewBishopWhite(520,720)
    AllPlayerlist.add(WhiteBishop)
    WhitePlayerlist.add(WhiteBishop) 


    


#add the White queen
    WhiteQueen=ViewQueenWhite(320,720)
    AllPlayerlist.add(WhiteQueen) 
    WhitePlayerlist.add(WhiteQueen) 

    


    WhiteKing=ViewKingWhite(420,720)
    AllPlayerlist.add(WhiteKing)
    WhitePlayerlist.add(WhiteKing) 



    
    
    
        #add the black pawn to the board

    for i in range(20,800,100):
        BlackPawn=ViewPawnBlack(i,120)
        AllPlayerlist.add(BlackPawn) 
        BlackPlayerlist.add(BlackPawn)       

    #add the black Knight to the board

    BlackKnight=ViewKnightBlack(120,20)
    AllPlayerlist.add(BlackKnight) 
    BlackPlayerlist.add(BlackKnight)       

    BlackKnight=ViewKnightBlack(620,20)
    AllPlayerlist.add(BlackKnight) 
    BlackPlayerlist.add(BlackKnight)       

    
    #add the black Steeple to the board

    
    BlackSteeple=ViewSteepleBlack(20,20)
    AllPlayerlist.add(BlackSteeple) 
    BlackPlayerlist.add(BlackSteeple)       

    BlackSteeple=ViewSteepleBlack(720,20)
    AllPlayerlist.add(BlackSteeple)
    BlackPlayerlist.add(BlackSteeple)       


#add bishop





    BlackBishop=ViewBishopBlack(220,20)
    AllPlayerlist.add(BlackBishop) 
    BlackPlayerlist.add(BlackBishop)       

    BlackBishop=ViewBishopBlack(520,20)
    AllPlayerlist.add(BlackBishop)
    BlackPlayerlist.add(BlackBishop)       


    


#add the black queen
    BlackQueen=ViewQueenBlack(320,20)
    AllPlayerlist.add(BlackQueen) 
    BlackPlayerlist.add(BlackQueen)       

    

#add black king
    BlackKing=ViewKingBlack(420,20)
    AllPlayerlist.add(BlackKing)
    BlackPlayerlist.add(BlackKing)       





    run=True
    clock=pygame.time.Clock()
    
    
    
    while(run==True):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

        if event.type==pygame.MOUSEBUTTONDOWN \
            and event.button==LEFT:
                y,x=pygame.mouse.get_pos()
                x,y=roundxy(x,y)
                Pos_From_To.append((x,y))
                flag_two=0

                print(x,y)
                if(len(Pos_From_To)==2):

                    if(board.BoardGame[x,y]==None):
                        flag_two=1
                    Flag=board.MovePlayer(Pos_From_To[0], Pos_From_To[1])
                    X,Y=Pos_From_To[0]
                    x,y=Pos_From_To[1]
                    Pos_From_To.clear()                  
                        
                    if (Flag==False):
                        Pos_From_To.clear()

                    if(Flag==True):
                        x,y=conversion(x,y)
                        X,Y=conversion(X,Y)


                        for enemy in AllPlayerlist:
                            if(enemy.GetLoc()==(Y,X)):
                                enemy.UpdateLoc(y,x)
                                team=enemy.GetTeam()
#here i want to delete from the view 
#panel the black player if somone eat them
                                if(flag_two==0):
                                    if(team==True):
                                        for black_player in BlackPlayerlist:
                                            if(black_player.GetLoc()==(y,x)):
                                                black_player.kill()
                                    else:
                                        for white_player in WhitePlayerlist:
                                            if(white_player.GetLoc()==(y,x)):
                                                white_player.kill()
                        
                      

                            
                            
                                


                            
                
                    
        BoardChess.draw_squres(WIN)
        pygame.display.update()
        AllPlayerlist.draw(WIN)
        pygame.display.flip()
        clock.tick(FPS)

        #pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main() 


