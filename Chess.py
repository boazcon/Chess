# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 23:31:43 2021

@author: boaz cohen!
"""
from abc import ABC ,abstractmethod
import numpy as np
from minmax import random_move, heuristic_calculate
class Controller():
    pass

def roundx(x,y):
    x = int(x / 100)
    y = int(y / 100)

    print(x,y)
    

class Board():
    Whites = []
    Blacks = [] 
    sum_black=-10390
    sum_white=10390
    Move=True
    BoardGame = np.empty((8,8), dtype=np.object)
    #oreder the board
    def __init__(self):
#here I make the king and put in pos ,and add him to list

        KingWhite = King(True,[7,4],10000)
        KingBlack = King(False,[0,4],-10000)
        self.BoardGame[7,4] = KingWhite
        self.Whites.append(KingWhite)
        self.BoardGame[0,4] = KingBlack
        self.Blacks.append(KingBlack)
        
        #here I make the Queen and put in pos ,and add him to list

        QueebWhite = Queen(True,[7,3],90)
        QueenBlack = Queen(False,[0,3],-90)
        self.BoardGame[7,3] = QueebWhite
        self.Whites.append(QueebWhite)
        self.BoardGame[0,3] = QueenBlack
        self.Blacks.append(QueenBlack)
        
        
        
#here I make the steeple(Tura) and put in pos ,and add him to list
        team = True
        SteepleWhite1 = Steeple(team, [7,7],50)
        SteepleWhite2 = Steeple(team, [7,0],50)
        self.Whites.append(SteepleWhite1)
        self.Whites.append(SteepleWhite2)
        self.BoardGame[7,7] = SteepleWhite1
        self.BoardGame[7,0] = SteepleWhite2
        
        
        team = False
        SteepleBlack1 = Steeple(team, [0,7],-50)
        SteepleBlack2 = Steeple(team, [0,0],-50)
        self.Blacks.append(SteepleBlack1)
        self.Blacks.append(SteepleBlack2)
        self.BoardGame[0,7] = SteepleBlack1
        self.BoardGame[0,0] = SteepleBlack2
        
        
        
#here I make the Knight and put in pos ,and add him to list

        team = True
        KnightWhite1 = Knight(team, [7,1],30)
        KnightWhite2 = Knight(team, [7,6],30)
        self.Whites.append(KnightWhite1)
        self.Whites.append(KnightWhite2)
        self.BoardGame[7,1] = KnightWhite1
        self.BoardGame[7,6] = KnightWhite2
        
        
        team = False
        KnightBlack1 = Knight(team, [0,1],-30)
        KnightBlack2 = Knight(team, [0,6],-30)
        self.Blacks.append(KnightBlack1)
        self.Blacks.append(KnightBlack2)
        self.BoardGame[0,1] = KnightBlack1
        self.BoardGame[0,6] = KnightBlack2


#here I make the Bishops and put in pos ,and add him to list
        team = True
        BishopsWhite1 = Bishop(team, [7,2],30)
        BishopWhite2 = Bishop(team, [7,5],30)
        self.Whites.append(BishopsWhite1)
        self.Whites.append(BishopWhite2)
        self.BoardGame[7,2] = BishopsWhite1
        self.BoardGame[7,5] = BishopWhite2


        
        team = False
        BishopBlack1 = Bishop(team, [0,2],-30)
        BishopBlack2 = Bishop(team, [0,5],-30)
        self.Blacks.append(BishopBlack1)
        self.Blacks.append(BishopBlack2)
        self.BoardGame[0,2] = BishopBlack1
        self.BoardGame[0,5] = BishopBlack2




#here I make the pawns and put in pos ,and add him to list
        team = False
        for i in range(8):
            pawn = Pawn(team,[1,i],-10)
            self.BoardGame[1,i] = pawn
            self.Blacks.append(pawn)
            
            
        team = True
        for i in range(8):
            pawn = Pawn(team,[6,i],10)
            self.BoardGame[6,i] = pawn
            self.Whites.append(pawn)

            
    #when u want to re-board
    def ReGame(self):
        pass
    
        
    
    def GetPlayerName(self,x,y):
        return self.BoardGame[x,y].GetName()
    
    #cheak if in square exist friend
   
   
    def NoFriend(self,NewPos,team): 
        x,y = NewPos
        player=self.BoardGame[x,y]
        if((player == None) or (team!=player.GetTeam())):
            return True
        else:
            return False
    
    
     #cheak if in square exist enemy
    def NoEnemy(self,NewPos,team):
        print("newpos", NewPos)
        x,y=NewPos
        print("x and y:",x,y)
        if(self.BoardGame[x,y] == None):
            return True
        else:
            player = self.BoardGame[NewPos]
            Team = player.GetTeam()
            if(team == Team):
                return True
        return False
    

#בדיקה אחרי מהלך של המלך, לבדוק אם *הוא* באיום
    def CheckForKing(self,team,NewPos):
        #בדיקה אם כתוצאה מתזוזת המלך הוא נכנס לאיום. הקוד גם מכסה " בריחה " של המלך משבצת נוספת , לוודא שאם הוא נמצא כרגע באיום והוא בורח למקום אחר(עם אותו איום, כג' על אותו קו) שעדיין יהיה false
        
        KingThreatBool=True
        if(team == True):
            KingW=self.Whites[0]
            X,Y = KingW.GetPos()
            t,z = NewPos
            player = self.BoardGame[t,z]  
            PosNow=X,Y
            self.BoardGame[X,Y] = None
            self.BoardGame[t,z] = KingW
            for Element in self.Blacks:
                if((Element.GetName() == "Steeple") or (Element.GetName() == "Queen") or (Element.GetName() == "Bishop")or (Element.GetName() == "Knight")or(Element.GetName() == "Pawn")):
                    KingThreatBool=Element.IsValidMove(NewPos,self,0)
                    if(KingThreatBool==False):
                        KingW.SetPos(PosNow)
                        self.BoardGame[t,z] = player
                        self.BoardGame[X,Y] = KingW
                        return False
            self.BoardGame[t,z] = player
            self.BoardGame[X,Y]=KingW
            return True
        
        if(team == False):
            KingB=self.Blacks[0]
            X,Y = KingB.GetPos()
            t,z = NewPos
            player = self.BoardGame[t,z]  

            PosNow=X,Y
            self.BoardGame[X,Y] = None
            self.BoardGame[t,z] = KingB
            for Element in self.Whites:
                if((Element.GetName() == "Steeple") or (Element.GetName() == "Queen") or (Element.GetName() == "Bishop")or (Element.GetName() == "Knight")or(Element.GetName() == "Pawn")):
                    KingThreatBool=Element.IsValidMove(NewPos,self,0)
                    if(KingThreatBool==False):
                        print(Element.GetName())
                        KingB.SetPos(PosNow)
                        self.BoardGame[t,z]= player
                        self.BoardGame[X,Y]=KingB
                        return False
            self.BoardGame[t,z] = player
            self.BoardGame[X,Y] = KingB
            return True

                    
    #בדיקה אם כתוצאה מהמהלך המלך תחת איום
    def KingTreat(self,team,player,NewPos):
    
        KingThreatBool=True
        X,Y = player.GetPos()
        t,z = NewPos
        PosNow=X,Y
        self.BoardGame[X,Y] = None
        self.BoardGame[t,z] = player
        

            

        if(team == True):
            KingW = self.Whites[0]
            
            for Element in self.Blacks:
                   
                if((Element.GetName() == "Steeple") or (Element.GetName() == "Queen") or (Element.GetName() == "Bishop")or (Element.GetName() == "Knight")or(Element.GetName() == "Pawn")):                        #בודק האם המלך (שהפך למלכה לצורך הבדיקה)-יכול לאכול את הרץ או הצריח או המלכה
                       #שורת הקוד הבאה בודק האם האיום נאכל במהלך האחרון
                        if(NewPos==Element.GetPos()):
                            break
                        #(יש מקרה קצה נוסף שהשורה לעיל-228-לא מכסה.
                        #המקרה הוא שאם אחד הכלים של הלבן זז, וכתוצאה מזה,"נולדו" 2 מקומות שמהם יש איום על המלך השחור.
                        #אז אם אזיז כלי של השחור על אחד הכלים המאיימים של הלבן, זה יאשר את המהלך, כיון שמבחינתו האיום סר.
                        #ולכן, מה שצריך לעשות זה להוסיף כאן בדיקה נוספת-for, שיבדוק האם ישנו עוד איום חוץ מהאיום שנמצא כרגע.
                        #לדעתי המקרה היחיד שבו מקרה קצה זה יכול לקרות זה כשמזיזים את הפרש, ופותחים ציר לאיום על המלך על כלי נוסף-בנוסף לאיום על ידי הפרש עצמו.
                        #ידיעה זו עשויה לעזור בכיצד לפתור את הבעיה.)
                        # ,אם הוא יכול, אז ההערך המתקבל הוא "שקר" ואם לא-אמת.

                        KingThreatBool = Element.IsValidMove(KingW.GetPos(),self,0)
                        if(KingThreatBool==False):  
                              break

            player.SetPos(PosNow)
            self.BoardGame[t,z]=None
            self.BoardGame[X,Y]=player                                  
            return KingThreatBool

        else:
        
               KingB = self.Blacks[0]
               for Element in self.Whites:
                 
                   if((Element.GetName() == "Steeple") or (Element.GetName() == "Queen") or (Element.GetName() == "Bishop")or (Element.GetName() == "Knight")or(Element.GetName() == "Pawn")):
                      #,אם הוא יכול, אז ההערך המתקבל הוא "שקר" ואם לא-אמת.
                           if(NewPos==Element.GetPos()):
                               break
                           

                           KingThreatBool = Element.IsValidMove(KingB.GetPos(),self,0)
                           if(KingThreatBool==False):  
                                 break


               player.SetPos(PosNow)
               self.BoardGame[t,z]=None
               self.BoardGame[X,Y]=player
               return KingThreatBool
           
           #פונקצייה שמשנה את התור
    def Change_turn(self):
        if(self.Move==True):
            self.Move=False
        else:
            self.Move=True
#פונקצייה שבודקת של מי התור עכשיו
    def Of_whom_the_turn(self,Team):
        if(self.Move==Team):
            return True
        else:
            return False
            
        
    
    def MovePlayer(self,PosNow,PosTarget):
        x,y = PosTarget  
        X ,Y = PosNow
        if(x < 0 or x > 7  or y < 0 or y > 7):
            print("out of range")
            return False
            
        player = self.BoardGame[X,Y]
        RemoveMe = self.BoardGame[x,y]
        if(player == None):
            print("no player there.")
            return False
        turn=self.Of_whom_the_turn(player.GetTeam())
        if(turn==False):
           print("its not your turn")
        else:
            IsValid = player.IsValidMove(PosTarget,self)
            if(IsValid == True):
                print("player,", player,"move from:" ,PosNow,"to:",PosTarget)

                self.Change_turn()
                self.BoardGame[PosTarget] = self.BoardGame[PosNow]
                self.BoardGame[PosNow] = None
                player.SetPos(PosTarget)
                if(RemoveMe == None):
                    return True
                else:
                    team = RemoveMe.GetTeam()
                    if(team == True):
                        self.Whites.remove(RemoveMe)
                        self.sum_white=self.sum_white-RemoveMe.GetValue()
                        del RemoveMe
                        print("total value game: ",self.sum_black+self.sum_white)

                        return True
                        
                    elif(team == False):
                        self.Blacks.remove(RemoveMe)
                        self.sum_black=self.sum_black-RemoveMe.GetValue()
                        del RemoveMe
                        print("total value game: ", self.sum_black+self.sum_white)

                        return True
                
            else:
                print("the" ,player.GetName(),"cant move to there!cheak for anoter option")
                return False

          
        
            
class Players(ABC):
    __value=None
    __pos = None,None
    __team = None #true is white
    __name = None 
    def __init__(self,team,pos,value):
        self.team = team
        self.pos = pos
        self.value = value
        
    def __del__(self):
       pass
   
    def GetName(self):
        return self.name
    
    def GetValue(self):
        return self.value
    
    def SetPos(self,NewPos):
        self.pos = NewPos
    def GetPos(self):
        return self.pos
    def SetTeam(self,Boolean):
        self.team = Boolean
    def GetTeam(self):
        return self.team
    @abstractmethod
    def IsValidMove(self):
        pass
    @abstractmethod
    def set_of_valid_moves(self):
        pass
    
    
           

class King(Players):
    
    name = "King"
    
# Check if the move is Valid for this player.

    def IsValidMove(self,NewPos,Board,Flag=1):
        x,y = self.GetPos()
        X,Y = NewPos
        team = self.GetTeam()
        #print("newpos", NewPos)
       # print("firs,",Board.BoardGame)
        
        if(False==Board.CheckForKing(team,NewPos)):
            print("invalid move,cheak another option")
            return False
        
        if(((x == X - 1) and (y == Y) and (Board.NoFriend(NewPos,team))) or ((x == X + 1) and (y == Y) and (Board.NoFriend(NewPos,team)) ) or ((y == Y - 1) and (x == X) and (Board.NoFriend(NewPos,team)) ) or ((y == Y + 1) and (x == X) and (Board.NoFriend(NewPos,team)) ) or ((y == Y + 1) and (x == X + 1) and (Board.NoFriend(NewPos,team)) ) or ((y == Y - 1) and (x == X - 1) and (Board.NoFriend(NewPos,team)) ) or ((y == Y + 1) and (x == X - 1) and (Board.NoFriend(NewPos,team)) ) or ((y == Y - 1) and (x == X + 1) and (Board.NoFriend(NewPos,team)) )):
            return True
        #TODO have Hazracha..
    def set_of_valid_moves(self):
        x,y = self.GetPos()
        return [[x-1,y],[x+1,y],[x,y-1],[x,y+1],[x-1,y-1],[x+1,y+1],[x-1,y+1],[x+1,y-1]]        
        
class Steeple(Players): #Tura..

    name = "Steeple"
#cheak if the move is Valid for this player
    
    def IsValidMove(self,NewPos,Board,Flag=1):
        x,y = self.GetPos()
        X,Y = NewPos
        team = self.GetTeam()
        if(Flag==1):
            if(((x == X) and (y != Y) and (Board.NoFriend(NewPos,team)) and (self.NoPlayersInWay(NewPos,Board)) and (Board.KingTreat(team,self,NewPos)))
            or((x != X) and (y == Y) and (Board.NoFriend(NewPos,team)) and (self.NoPlayersInWay(NewPos,Board)) and (Board.KingTreat(team,self,NewPos)))):
                return True
            else:
                return False
        elif(Flag==0):
            if((x == X) and (Y != y) and (Board.NoFriend(NewPos,team))  and (self.NoPlayersInWay(NewPos,Board)) or ((x != X) and (Y == y) and (Board.NoFriend(NewPos,team)) and (self.NoPlayersInWay(NewPos,Board)))):
                return False
            else:
                return True

               
            
        
        
    def NoPlayersInWay(self,NewPos,Board):

        x,y = self.GetPos()
        X,Y = NewPos
        team = self.GetTeam()
        if(x > X) and (y == Y):
            
             for i in range(x-1,X,-1):
                 x=x-1
                 print("range:",range(x-1,X),"x,y",x,y,"i:",i)
                 if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                    return False
             return True
       
             
         
        if(x < X) and (y == Y):
             for i in range(x,X-1):
                 x=x+1
                 print("range:",range(x-1,X),"x,y",x,y,"i:",i)
    
                 if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                        return False
    
             return True 
        if(y > Y) and (X == x):
             for i in range(y-1,Y,-1):
                 y=y-1
                 print("range:",range(x-1,X),"x,y",x,y,"i:",i)
                 
                 if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                        return False
    
             return True 
             
        if(y < Y) and (X == x):
             for i in range(y,Y-1):
                 y=y+1
                 print("range:",range(x-1,X),"x,y",x,y,"i:",i)
    
                 if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                        return False

             return True 
        
        
        else:
            return False
     

        
    def set_of_valid_moves(self):
        
        y,x = self.GetPos()
        #לצורך בדיקה בלבלד!!!!
        return [[x,y+1],[x,y+2]]


class Bishop(Players): #runner..
    name = "Bishop"
#cheak if the move is Valid for this player

    def IsValidMove(self,NewPos,Board,Flag=1):
        x,y = self.GetPos()
        X,Y = NewPos
        team = self.GetTeam()
        if(Flag==1):
            if((abs(x - X) == abs(y - Y)) and (Board.NoFriend(NewPos,team)) and (self.NoPlayersInWay(NewPos, Board)) and (Board.KingTreat(team,self,NewPos))):
                return True
            else:
                return False


        elif(Flag==0):
            if((abs(x - X) == abs(y - Y)) and (self.NoPlayersInWay(NewPos, Board))):
                return False
            else:
                return True


        
    def NoPlayersInWay(self,NewPos,Board):
        x,y = self.GetPos()
        X,Y = NewPos
        team = self.GetTeam()
        if(x < X) and (y < Y):
           
            for i in range(abs(x - X)-1):
                x,y=x+1,y+1
                if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                    return False
              
            return True

           
            
        if(x > X) and (y < Y):
            
            for i in range(abs(x - X)-1):
                x,y=x-1,y+1
                if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                    return False

            return True

               
        
        if(x < X) and (y > Y):
            
            for i in range(abs(x - X)-1):
                x,y=x+1,y-1
                if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                   return False

            return True

        if(x > X) and (y > Y):
            for i in range(abs(x - X)-1):
                x,y=x-1,y-1

                if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                   return False

            return True
        
        
    def set_of_valid_moves(self):
        y,x = self.GetPos()
        #לצורך בדיקה בלבלד!!!!

        return [[x+1,y+1]]
        


class Queen(Players):  
    
    
    name = "Queen"
    #cheak if the move is Valid for this player

    def IsValidMove(self,NewPos,Board,Flag=1):
        x,y = self.GetPos()
        X,Y = NewPos
        team = self.GetTeam()
        
        if (Flag == 1):
            if(abs(x - X) == abs(y - Y) and (Board.NoFriend(NewPos,team)) and (self.NoPlayersInWay(NewPos,Board)) and (Board.KingTreat(team,self,NewPos)) 
               or ((x == X) and (y != Y) and (Board.NoFriend(NewPos,team)) and (self.NoPlayersInWay(NewPos,Board))) and (Board.KingTreat(team,self,NewPos))
              or ((x != X) and (y == Y) and (Board.NoFriend(NewPos,team)) and (self.NoPlayersInWay(NewPos,Board))) and (Board.KingTreat(team,self,NewPos))):
               return True
            else:
                return False
            #flag =0 אומר שהמלכה משמשת כרגע בבדיקה שאין שח על המלך כתוצאה מתזוזה של שחקן מסוים
        elif(Flag == 0):
            
            if(abs(x - X) == abs(y - Y) and (Board.NoFriend(NewPos,team)) and (self.NoPlayersInWay(NewPos,Board))
              or ((x == X) and (y != Y) and (Board.NoFriend(NewPos,team)) and (self.NoPlayersInWay(NewPos,Board))) 
              or ((x != X) and (y == Y) and (Board.NoFriend(NewPos,team)) and (self.NoPlayersInWay(NewPos,Board)))):
                return False
            else:
                return True
            
    def NoPlayersInWay(self,NewPos,Board):
       x,y = self.GetPos()
       X,Y = NewPos




       team = self.GetTeam()
       #cheak if its runner move
       if(x < X) and (y < Y):
           
            for i in range(abs(x - X)-1):
                x, y = x+1, y+1
                if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                    return False
              
            return True

           
            
       if(x > X) and (y < Y):
            
            for i in range(abs(x - X) -1):
                x,y=x-1,y+1
                if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                    return False

            return True

               
        
       if(x < X) and (y > Y):
            
            for i in range(abs(x - X)-1):
                x,y=x+1,y-1

                if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                   return False

            return True

       if(x > X) and (y > Y):
            for i in range(abs(x - X)-1):
                x,y=x-1,y-1

                if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                   return False

            return True
          
                   
   #cheak if its steeple move
       elif((x == X) and (Y != y) or ((x != X) and (Y == y))):
           if(x > X) and (y == Y):
               
            for i in range(x-1,X,-1):
                x=x-1
                if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                   return False
            return True
          
                
            
           if(x < X) and (y == Y):
             for i in range(x,X-1):
                x=x+1

                if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                       return False

             return True 
           if(y > Y) and (X == x):
               
                for i in range(y-1,Y,-1):
                    y=y-1
                    if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                           return False
    
                return True 
                
           if(y < Y) and (X == x):
            for i in range(y,Y-1):
                y=y+1
                if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                       return False

            return True 
        
        
           else:
              return False
     
       
    def set_of_valid_moves(self):
        y,x = self.GetPos()
        #לצורך בדיקה בלבלד!!!!
        return [[x,y+1],[x,y+2]]
      
       
       
class Pawn(Players):  
    name = "Pawn"
#cheak if the move is Valid for this player
    
    
    FirstMove = True
   
    def IsFirsMove(self,Board):
        y,x = self.GetPos()
        if(y == 6) or (y == 1):
            return True
    


    def IsValidMove(self,NewPos,Board,Flag=1):
        y,x = self.GetPos()
        Y,X = NewPos
      
        team = self.GetTeam()
        if(Flag==1):
            if(((x == X) and (Y == y + 1) and (team == False) and (Board.NoEnemy(NewPos,team)) and (Board.NoFriend(NewPos,team)) and (Board.KingTreat(team,self,NewPos))) 
               or ((x == X) and (Y == y - 1) and (team == True) and (Board.NoEnemy(NewPos,team)) and (Board.NoFriend(NewPos,team)) and (Board.KingTreat(team,self,NewPos))) 
               or ((x == X) and (Y == y + 2) and (team == False) and (Board.NoEnemy(NewPos,team)) and (self.IsFirsMove(Board)) and (Board.NoFriend(NewPos,team)) and (Board.KingTreat(team,self,NewPos)))
               or ((x == X) and (Y == y - 2) and (team == True) and (Board.NoEnemy(NewPos,team)) and (self.IsFirsMove(Board)) and (Board.NoFriend(NewPos,team)) and (Board.KingTreat(team,self,NewPos))) 
               or ((x == X + 1) and (y == Y + 1) and (team == True) and (False == Board.NoEnemy(NewPos,team)) and (Board.KingTreat(team,self,NewPos))) 
               or ((x == X - 1) and (y == Y + 1) and (team == True) and (False == Board.NoEnemy(NewPos,team)) and (Board.KingTreat(team,self,NewPos))) 
               or ((x == X + 1) and (y == Y - 1) and (team == False) and (False == Board.NoEnemy(NewPos,team)) and (Board.KingTreat(team,self,NewPos))) 
               or ((x == X - 1) and (y == Y - 1) and (team == False) and (False == Board.NoEnemy(NewPos,team)) and (Board.KingTreat(team,self,NewPos)))):
                return True
            else:
                return False
        elif(Flag==0):
            if(((x == X + 1) and (y == Y + 1) and (team == True)) 
               or ((x == X - 1) and (y == Y + 1) and (team == True)) 
               or ((x == X + 1) and (y == Y - 1) and (team == False)) 
               or ((x == X - 1) and (y == Y - 1) and (team == False))):
                return False
            else:
                return True
    def set_of_valid_moves(self):
        y,x = self.GetPos()

        if self.FirstMove:
            return [[x+2,y],[x+1,y+1],[x+1,y-1],[x+1,y]]
        else:
            return [[x+1,y+1],[x-1,y+1],[x,y+1]]

        
#TODO add en passant option!

class Knight(Players):  #horse..


    name = "Knight"
    
 #cheak if the move is Valid for this player
    def IsValidMove(self,NewPos,Board,flag=1):
        y,x = self.GetPos()
        Y,X = NewPos

        team = self.GetTeam()
        if(flag==1):
            
            if(((x == X + 1) and (y == Y + 2) and (Board.NoFriend(NewPos,team)) and (Board.KingTreat(team,self,NewPos))) or ((x == X + 1) and (y == Y - 2) and (Board.KingTreat(team,self,NewPos)) and (Board.NoFriend(NewPos,team)) and (Board.KingTreat(team,self,NewPos))) or ((x == X - 1) and (y == Y + 2) and (Board.NoFriend(NewPos,team)) and (Board.KingTreat(team,self,NewPos))) or ((x == X - 1) and (y == Y - 2) and (Board.NoFriend(NewPos,team)) and (Board.KingTreat(team,self,NewPos))) or ((y == Y + 1) and (x == X + 2) and (Board.NoFriend(NewPos,team)) and (Board.KingTreat(team,self,NewPos))) or ((y == Y + 1) and (x == X - 2) and (Board.NoFriend(NewPos,team)) and (Board.KingTreat(team,self,NewPos))) or ((y == Y - 1) and (x == X + 2) and (Board.NoFriend(NewPos,team)) and (Board.KingTreat(team,self,NewPos))) or ((y == Y - 1) and (x == X - 2) and (Board.NoFriend(NewPos,team)) and (Board.KingTreat(team,self,NewPos)))):
                return True
            else:
                return False
        if(flag==0):
            if(((x == X + 1) and (y == Y + 2)  and (Board.NoFriend(NewPos,team))) or ((x == X + 1) and (y == Y - 2) and (Board.NoFriend(NewPos,team))) or ((x == X - 1) and (y == Y + 2) and (Board.NoFriend(NewPos,team))) or ((x == X - 1) and (y == Y - 2) and (Board.NoFriend(NewPos,team))) or ((y == Y + 1) and (x == X + 2) and (Board.NoFriend(NewPos,team))) or ((y == Y + 1) and (x == X - 2) and (Board.NoFriend(NewPos,team))) or ((y == Y - 1) and (x == X + 2) and (Board.NoFriend(NewPos,team))) or ((y == Y - 1) and (x == X - 2) and (Board.NoFriend(NewPos,team)))):
                return False
            else:
                return True

    
    
    def set_of_valid_moves(self):
        y,x = self.GetPos()
        return [[x+1,y+2],[x+1,y-2],[x-1,y+2],[x-1,y-2],[x+2,y+1],[x+2,y-1],[x-2,y+1],[x-2,y-1]]
        

        
    
    
def main():
     board = Board()
     
     board.MovePlayer((6,5), (4,5))
     board.MovePlayer((1,1), (2,1))

    
   
    
if __name__ == "__main__":
     main() 
    
   
    
    
    