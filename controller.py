# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 11:37:01 2022

@author: boaz
"""

from View import * # NOQA 

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
                                                
                           
                        #pc move
                        
        #                 n=0
        #                 while(n != 1):
        #                     flag_two = 0
        #                     PosNow, PosTarget = random_move(board)
        #                     print(PosNow, PosTarget)
        #
        #
        #                     X, Y = PosNow
        #                     x, y= PosTarget
        #                     if(x<0 or x>7  or y<0 or y>7):
        #                         print("out of range")
        #                         continue
        #
        #
        #                     Flag=board.MovePlayer(PosNow, PosTarget)
        #                     if(Flag==True):
        #                         if(board.BoardGame[x,y]==None):
        #                             flag_two=1
        #                         print(flag_two, "flag_two")
        #                         n=1
        #                         X,Y=conversion(X, Y)
        #                         x,y=conversion(x, y)
        #                         for enemy in AllPlayerlist:
        #                             if(enemy.GetLoc()==(Y,X)):
        #                                 enemy.UpdateLoc(y,x)
        #                                 team=enemy.GetTeam()
        # #here i want to delete from the view
        # #panel the black player if somone eat them
        #                                 if(flag_two==0):
        #                                     if(team==True):
        #                                         for black_player in BlackPlayerlist:
        #                                             if(black_player.GetLoc()==(y,x)):
        #                                                 black_player.kill()
        #                                     else:
        #                                         for white_player in WhitePlayerlist:
        #                                             if(white_player.GetLoc()==(y,x)):
        #                                                 white_player.kill()
        #
        #
        #                     else:
        #                         continue
                         
                            
                            
                            
                                


                            
                
                    
        BoardChess.draw_squres(WIN)
        pygame.display.update()
        AllPlayerlist.draw(WIN)
        pygame.display.flip()
        clock.tick(FPS)

        #pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main() 
