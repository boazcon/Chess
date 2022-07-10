# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 20:12:44 2022
this script will be AI-minmax a/b purning to my chess
now he make random moves
@author: boaz cohen
"""
import random

from Chess import * 



# פונקצייה שמחשבת את איכות המהלך על ידי חישוב כמות הכלים על הלוח
def heuristic_calculate(board):
    
    return board.sum_black-board.sum_white
    
    pass

def random_move(board):
    max_move=None
    number_of_player = len(board.Blacks)
    player_to_move = board.Blacks[random.randint(0, number_of_player-1)]
    set_of_valid_moves = player_to_move.set_of_valid_moves()
    random_move_from_the_set = random.randint(0, len(set_of_valid_moves)-1)
    #print("move numnber of valid move,", random_move_from_the_set)
    #print("from to:", player_to_move.GetPos(), set_of_valid_moves[random_move_from_the_set])
    return player_to_move.GetPos(), set_of_valid_moves[random_move_from_the_set]
    
    
    
                
                
                

                
            
                

    


