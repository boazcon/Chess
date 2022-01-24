# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 23:31:43 2021

@author: boaz cohen!
"""
from abc import ABC ,abstractmethod
import numpy as np
class Controller():
    pass

def roundx(x,y):
    x = int(x / 100)
    y = int(y / 100)

    print(x,y)
    

class Board():
    Whites = []
    Blacks = [] 
    Move=True
    #TODO : have to put in private status after
    BoardGame = np.empty((8,8), dtype=np.object)
    #oreder the board
    def __init__(self):
#here I make the king and put in pos ,and add him to list

        KingWhite = King(True,[7,4])
        KingBlack = King(False,[0,4])
        self.BoardGame[7,4] = KingWhite
        self.Whites.append(KingWhite)
        self.BoardGame[0,4] = KingBlack
        self.Blacks.append(KingBlack)
        
        #here I make the Queen and put in pos ,and add him to list

        QueebWhite = Queen(True,[7,3])
        QueenBlack = Queen(False,[0,3])
        self.BoardGame[7,3] = QueebWhite
        self.Whites.append(QueebWhite)
        self.BoardGame[0,3] = QueenBlack
        self.Blacks.append(QueenBlack)
        
        
        
#here I make the steeple(Tura) and put in pos ,and add him to list
        team = True
        SteepleWhite1 = Steeple(team, [7,7])
        SteepleWhite2 = Steeple(team, [7,0])
        self.Whites.append(SteepleWhite1)
        self.Whites.append(SteepleWhite2)
        self.BoardGame[7,7] = SteepleWhite1
        self.BoardGame[7,0] = SteepleWhite2
        
        
        team = False
        SteepleBlack1 = Steeple(team, [0,7])
        SteepleBlack2 = Steeple(team, [0,0])
        self.Blacks.append(SteepleBlack1)
        self.Blacks.append(SteepleBlack2)
        self.BoardGame[0,7] = SteepleBlack1
        self.BoardGame[0,0] = SteepleBlack2
        
        
        
#here I make the Knight and put in pos ,and add him to list

        team = True
        KnightWhite1 = Knight(team, [7,1])
        KnightWhite2 = Knight(team, [7,6])
        self.Whites.append(KnightWhite1)
        self.Whites.append(KnightWhite2)
        self.BoardGame[7,1] = KnightWhite1
        self.BoardGame[7,6] = KnightWhite2
        
        
        team = False
        KnightBlack1 = Knight(team, [0,1])
        KnightBlack2 = Knight(team, [0,6])
        self.Blacks.append(KnightBlack1)
        self.Blacks.append(KnightBlack2)
        self.BoardGame[0,1] = KnightBlack1
        self.BoardGame[0,6] = KnightBlack2


#here I make the Bishops and put in pos ,and add him to list
        team = True
        BishopsWhite1 = Bishop(team, [7,2])
        BishopWhite2 = Bishop(team, [7,5])
        self.Whites.append(BishopsWhite1)
        self.Whites.append(BishopWhite2)
        self.BoardGame[7,2] = BishopsWhite1
        self.BoardGame[7,5] = BishopWhite2


        
        team = False
        BishopBlack1 = Bishop(team, [0,2])
        BishopBlack2 = Bishop(team, [0,5])
        self.Blacks.append(BishopBlack1)
        self.Blacks.append(BishopBlack2)
        self.BoardGame[0,2] = BishopBlack1
        self.BoardGame[0,5] = BishopBlack2




#here I make the pawns and put in pos ,and add him to list
        team = False
        for i in range(8):
            pawn = Pawn(team,[1,i])
            self.BoardGame[1,i] = pawn
            self.Blacks.append(pawn)
            
            
        team = True
        for i in range(8):
            pawn = Pawn(team,[6,i])
            self.BoardGame[6,i] = pawn
            self.Whites.append(pawn)

            
     
            
        
        
        
    #when u want to re-board
    def ReGame(self):
        pass
    
    
    
        
    #
    def GetPlayerName(self,x,y):
        return self.BoardGame[x,y].GetName()
    
    #cheak if in square exist friend
   
   
    def NoFriend(self,NewPos,team): 
        x,y = NewPos
        player=self.BoardGame[x,y]
        if((player == None)or(team!=player.GetTeam())):
            return True
        else:
            return False
    
     #cheak if in square exist enemy
    def NoEnemy(self,NewPos,team):
        if(self.BoardGame[NewPos] == None):
            return True
        else:
            player = self.BoardGame[NewPos]
            Team = player.GetTeam()
            if(team == Team):
                return True
        return False

#בדיקה אחרי מהלך של המלך, לבדוק אם *הוא* באיום
    def CheckForKing(self,team,NewPos):
        KingThreatBool=True

        if(team == True):
            for Element in self.Blacks:
                   
                if((Element.GetName() == "Steeple") or (Element.GetName() == "Queen") or (Element.GetName() == "Bishop")or (Element.GetName() == "Knight")or(Element.GetName() == "Pawn")):
                    KingThreatBool=Element.IsValidMove(NewPos,self,0)
                    if(KingThreatBool==False):
                        print(Element.GetName())
                        return False
            return True
        
        if(team == False):
            for Element in self.Whites:
                if((Element.GetName() == "Steeple") or (Element.GetName() == "Queen") or (Element.GetName() == "Bishop")or (Element.GetName() == "Knight")or(Element.GetName() == "Pawn")):
                    KingThreatBool=Element.IsValidMove(NewPos,self,0)
                    if(KingThreatBool==False):
                        print(Element.GetName())
                        return False
            return True

                    
    #בדיקה אם כתוצאה מהמהלך המלך תחת איום
    def KingTreat(self,team,player,NewPos):
    #    return True
       # if(player.GetName=="Knight"):
       
        KingThreatBool=True
        X,Y = player.GetPos()
        t,z = NewPos
        PosNow=X,Y
        self.BoardGame[X,Y] = None
        self.BoardGame[t,z] = player
        

            

        if(team == True):
            KingW = self.Whites[0]
            #if(player.GetName()=="King"):
             #   player.SetPos(NewPos)
            for Element in self.Blacks:
                   
                if((Element.GetName() == "Steeple") or (Element.GetName() == "Queen") or (Element.GetName() == "Bishop")or (Element.GetName() == "Knight")or(Element.GetName() == "Pawn")):                        #בודק האם המלך (שהפך למלכה לצורך הבדיקה)-יכול לאכול את הרץ או הצריח או המלכה
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
                          # if(player.GetName()=="King"):
                           #    player.SetPos(NewPos)
                            #   print(player.GetPos())

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
        #we want to remove this player from the list!
        player = self.BoardGame[PosNow]
        RemoveMe = self.BoardGame[PosTarget]
        
        if(player == None):
            
            print("no player there.")
            
            return False
        turn=self.Of_whom_the_turn(player.GetTeam())
        if(turn==False):
            print("its not your turn!!!liar!")
            return 
        else:
            
            
            IsValid = player.IsValidMove(PosTarget,self)
            
            if(IsValid == True):
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
                        del RemoveMe
                        return True
                        
                    elif(team == False):
                        self.Blacks.remove(RemoveMe)
                        del RemoveMe
                        return True
                
            else:
                print("the" ,player.GetName(),"cant move to there!cheak for anoter option")
                return False

          
        
            
class Players(ABC):
    
    __pos = None,None
    __team = None #true is white
    __name = None 
    #TODO __En_Passant=False:: to devlop after
    def __init__(self,team,pos):
        self.team = team
        self.pos = pos
        
    def __del__(self):
       pass
   
    def GetName(self):
        return self.name
    
    
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
    
           

class King(Players):
    
    name = "King"
    
# Check if the move is Valid for this player.

    def IsValidMove(self,NewPos,Board,Flag=1):
        x,y = self.GetPos()
        X,Y = NewPos
        team = self.GetTeam()
        #TODO  bug fix-if exist threat on the king ,the king can run away one step from the threat.
        #and to fix the bug with the pawn-(simple).
       # lastbug??????--no
        
        if(False==Board.CheckForKing(team,NewPos)):
            print("invalid move,cheak another option")
            return False
        
      
        if(((x == X - 1) and (y == Y) and (Board.NoFriend(NewPos,team))) or ((x == X + 1) and (y == Y) and (Board.NoFriend(NewPos,team)) ) or ((y == Y - 1) and (x == X) and (Board.NoFriend(NewPos,team)) ) or ((y == Y + 1) and (x == X) and (Board.NoFriend(NewPos,team)) ) or ((y == Y + 1) and (x == X + 1) and (Board.NoFriend(NewPos,team)) ) or ((y == Y - 1) and (x == X - 1) and (Board.NoFriend(NewPos,team)) ) or ((y == Y + 1) and (x == X - 1) and (Board.NoFriend(NewPos,team)) ) or ((y == Y - 1) and (x == X + 1) and (Board.NoFriend(NewPos,team)) )):
            return True
        #TODO have Hazracha..

class Steeple(Players): #Tura..

    name = "Steeple"
#cheak if the move is Valid for this player
    
    def IsValidMove(self,NewPos,Board,Flag=1):
        x,y = self.GetPos()
        X,Y = NewPos
        team = self.GetTeam()
        if(Flag==1):
            if((x == X) and (Y != y) and (Board.NoFriend(NewPos,team)) and ((Board.KingTreat(team,self,NewPos))) and (self.NoPlayersInWay(NewPos,Board)) or ((x != X) and (Y == y) and ((Board.KingTreat(team,self,NewPos))) and (Board.NoFriend(NewPos,team)) and (self.NoPlayersInWay(NewPos,Board)))):

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
                print("range:",abs(x - X)-1,"x,y",x,y,"i:",i)
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
          
                   
   #cheak if its steeple move
       elif((x == X) and (Y != y) or ((x != X) and (Y == y))):
           if(x > X) and (y == Y):
               
            for i in range(x-1,X,-1):
                x=x-1
                print("range:",range(x-1,X),"x,y",x,y,"i:",i)
                Pos = i - 1,y
                if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                   return False
            return True
          
                
            
           if(x < X) and (y == Y):
            for i in range(x,X-1):
                x=x+1
                Pos = i,y
                print("range:",range(x-1,X),"x,y",x,y,"i:",i)

                if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                       return False

            return True 
           if(y > Y) and (X == x):
            for i in range(y-1,Y,-1):
                y=y-1
                print("range:",range(x-1,X),"x,y",x,y,"i:",i)

                Pos = x,i - 1
                
                if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                       return False

            return True 
                
           if(y < Y) and (X == x):
            for i in range(y,Y-1):
                y=y+1
                print("range:",range(x-1,X),"x,y",x,y,"i:",i)

                Pos = x,i + 1
                if((False == Board.NoFriend((x,y),team))or(False == Board.NoEnemy((x,y),team))):
                       return False

            return True 
        
        
           else:
              return False
     
       
       
       
       
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
            if(((x == X + 1) and (y == Y + 1) and (team == True) and ( Board.NoEnemy(NewPos,team))) 
               or ((x == X - 1) and (y == Y + 1) and (team == True) and (Board.NoEnemy(NewPos,team))) 
               or ((x == X + 1) and (y == Y - 1) and (team == False) and ( Board.NoEnemy(NewPos,team))) 
               or ((x == X - 1) and (y == Y - 1) and (team == False) and ( Board.NoEnemy(NewPos,team)))):
                return False
            else:
                return True

        
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

    
    
    
    
    
def main():
     board = Board()
     
     board.MovePlayer((7,4), (7,4))
     board.MovePlayer((7,4), (7,4))

     #board.MovePlayer((1,4), (2,4))
     #board.MovePlayer((6,5), (5,5))
    # board.MovePlayer((0,3), (4,7))
   #  board.MovePlayer((7,4), (6,3))
     


    #attantion!the left side is the Y ,and the right is X!
    
    
    
   
   # print(board.Whites)
    #[1],[2],[3],[6],[7]
   # print(board.Blacks[0])

    
    
     #board.MovePlayer((6,4), (5,4))
   # board.MovePlayer((7,3), (3,7))

    #board.MovePlayer((1,5), (2,5))
    #board.MovePlayer((2,0), (6,4))
    #board.MovePlayer((0,1), (2,2))
   # board.MovePlayer((0,0), (0,0))
    #print(board.BoardGame[0,0])
    
 #   board.MovePlayer((6,4), (5,4))
    #board.MovePlayer((7,3), (3,7))
   # board.MovePlayer((1,5), (2,5))

   # print(board.BoardGame[1,1])
   # board.MovePlayer((0,3), (3,0))
    #board.MovePlayer((0,2), (1,1))
   # board.MovePlayer((1,1), (0,2))
    



    
  
   











    
    #board.MovePlayer((0,0), (0,1))
    #board.MovePlayer((0,1), (0,0))


   # board.MovePlayer((0,6), (0,5))
    #board.MovePlayer((0,3), (3,0))

    #board.MovePlayer((6,3), (5,3))
  #  print(board.Whites)
   # print(board.Blacks)
   # board.MovePlayer((0,7), (0,5))




    #board.MovePlayer((0,1), (0,0))

    



    #board.MovePlayer((2,1), (3,1))
    #board.MovePlayer((3,1), (4,1))
    #board.MovePlayer((4,1), (5,1))
    #board.MovePlayer((5,1), (6,0))
    #board.MovePlayer((6,0), (7,1))
    #board.MovePlayer((6,6), (5,6))
    #board.MovePlayer((5,6), (4,6))
    #board.MovePlayer((4,6), (3,6))
    #board.MovePlayer((3,6), (2,6))
    #board.MovePlayer((6,6), (5,6))
    #board.MovePlayer((1,7), (0,6))



    
    #board.MovePlayer((2,2), (4,3))
    #board.MovePlayer((4,3), (6,4))
    
  

  #  print("---------------------------")
    
  # print(board.BoardGame)

    
   
    
if __name__ == "__main__":
     main() 
    
    #11/6 
    #keep cheaking the movement element!!
    #keep cheking the pawn movments and eating, and fix the functions 
    
    #(13/6)
    #after cheaking all the players, have to build the more conditions for movments(if another
    #player in the way) and after that to add the function:
    #KingThreat
    
    #14/6 have to add conditions for queen, and the func KingThreat
    #לתקן את הבעיה שמשום מה הוא מזיז לי מהליסט 
    
    
