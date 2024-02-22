# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 22:27:02 2021

@author: Linus
"""
import numpy as np
from random import randint
import matplotlib.pyplot as plt
import matplotlib.axes as ax
#import sys

nrow = 6
ncol = 7

"""
The starting turn number will be zero, which indicates Player 1's turn. The turn number can be changed to an odd number: i.e. 1, to start from Player 2 (the computer). 
"""
turn = 0 #keeps track of turn number

def make_board(nrow, ncol):
    """
    Returns the board when called.
    """
    game_board = np.zeros([nrow, ncol])
    return game_board

def place(board, row, col, player):
    """
    Returns the board (with a placed token represented by the player number)
    """
    board[row][col] = player
    return board

def valid_col(board, col):
    """
    Returns True/False depending on if the column is full
    """
    if min(board[:,col]) == 0:
        return True
    
    # if min(board[:,col]) != 0:
    return False
    
def next_open_row(board, col):
    """
    Returns the next avalible empty slot in the row for the token to be placed into
    """
    for i in range(nrow):
        if board[i][col] == 0:
            return i
        
    #return True

def full_board(board, row, col): 
    """     
    Returns True if the board is full.
    """
    if np.all(board) !=0:
        return True
            
    else:
        return False

def four_in_a_row(board, token):
    """
    A long winded function. Returns "True" if it detects that four tokens of the same number have been placed in a row.
    """
    board_height = len(board[0])
    board_width = len(board)

    #for vertical wins    
    for y in range(board_height):
        for x in range(board_width - 3):
            #print(token, board[x][y], board[x + 1][y], board[x + 2][y], board[x + 3][y])
            if board[x][y] == token and board[x + 1][y] == token and board[x + 2][y] == token and board[x+3][y] == token:
                #print('Vertical Win.')
                return True

    #for horizontal wins
    for x in range(board_width):
        for y in range(board_height - 3):
            #print(token, board[x][y], board[x][y + 1], board[x][y + 2], board[x][y + 3])
            if board[x][y] == token and board[x][y + 1] == token and board[x][y + 2] == token and board[x][y + 3] == token:
                #print('Horizontal Win.')
                return True
    
    #for diagonal wins (\)
    for x in range(board_width - 3):
        for y in range(board_height - 3):
            #print(token, board[x + 1][y + 1],board[x + 2][y + 2], board[x + 3][y + 3])
            if board[x][y] == token and board[x + 1][y + 1] == token and board[x + 2][y + 2] == token and board[x + 3][y + 3] == token:
                #print('Diagonal (\) Win.')
                return True
            
    #for diagonal wins (/)
    for x in range(board_width - 3):
        for y in range(board_height):
            #print(token, board[x + 1][y - 1],board[x + 2][y - 2], board[x + 3][y - 3])
            if board[x][y] == token and board[x + 1][y - 1] == token and board[x + 2][y - 2] == token and board[x + 3][y - 3] == token:
                #print('Diagonal (/) Win.')
                return True
            
    return False
    
game_board = make_board(nrow, ncol) 
#print(game_board) 

"""
Setting up the game loop
"""
win = False

draw = False

Troubleshoot = False

while not win or draw:
    if bool(four_in_a_row(game_board, 2)) == False and bool(four_in_a_row(game_board, 1)) == False:
        if turn % 2 == 0 and win == False:
            try:
                #print(turn)
                input_col = int(input('Please select a column number of your choice.'))
                print()
                assert input_col - 1 >= 0 and input_col <= ncol 
            except ValueError: #if a non-integer is inserted
                print()
                print("Invalid integer! Please input a column number from 1-7.")
                continue
            except AssertionError: #if an integer outside the vaild column range is inserted
                print("Not a valid column number! Please input a column number from 1-7.")
                continue
            
            input_col = input_col - 1 #converting human input into computer understandable input
            
            #else:
                #break
            
            if full_board(game_board, next_open_row, input_col) == True:
                   print('No more empty rows! Game is drawn')
                   if bool(draw) == False:
                       draw = not draw
              
                #input_col = input_col - 1 #converting human input into computer understandable input
                
            while not valid_col(game_board, input_col) and draw:
                try:
                    raise ValueError('Column Full')
                except ValueError:
                    print()
                    print('Column Full. Please select another column')
                    continue
                    
            #elif bool(valid_col(game_board, input_col)) == False and draw == False:
            else:
                #input_col = input_col - 1 #converting human input into computer understandable input
                row = next_open_row(game_board, input_col)
                place(game_board, row, input_col, 1)
                #print(game_board)
                #print(input_col)
                
        else:
            if win == False or draw == False: 
                if bool(four_in_a_row(game_board, 2)) == False:
                    print()
                    print('The Computer is making a move...') #if it is Player 2's turn, then the computer will be the one making the moves.
                    print()
                    # print(game_board)
                    # print(input_col)
                    
                    for c in range(1):
                        input_col = randint(0 , ncol - 1) #generate a random number between 0 to 6 (the number of columns - 1)
                        
                        if full_board(game_board, next_open_row, input_col) == True:
                            print('No more empty rows! Game is drawn')
                            if bool(draw) == False:
                                draw = not draw
                         
                        if bool(valid_col(game_board, input_col)) == True and draw == False:
                            row = next_open_row(game_board, input_col)
                            place(game_board, row, input_col, 2)
                            #print(game_board)
                            
                        elif bool(valid_col(game_board, input_col)) == False and draw == False:
                             print('Column Full. Computer is selecting another column...')
                             
                             
                else:
                    if win == False:
                        win = not win
                    
        print(game_board[::-1], flush = True)

        if Troubleshoot == True: # if Troubleshooting = True then these will be printed.
            print()
            print('Any winners?')
            if win == True:
                print('No.')
            print()
            print('Player 1 Win?')
            print(bool(four_in_a_row(game_board, 1))) #True if Connect 4 has been detected
            print()
            print('Player 2 Win?')
            print(bool(four_in_a_row(game_board, 2))) #True if connect 4 has been detected
            print()
            print('Board Full:')
            print(bool(full_board(game_board, next_open_row, input_col))) #True if board is full
            print()
            print('Valid Columns?')
            print(bool(valid_col(game_board, input_col))) #True if col is not full
            print()
            print('Next Open Row?')
            print(next_open_row(game_board, input_col))
            print()
        
        turn += 1 #adds a turn into the turn counter
        turn = turn % 2 #checking if the turn number's modulus
    
    else:
        if win == False:
            win = not win
else:
    if win == True and draw == False:
      #print(game_board)
      for i in range(len(game_board)):
          for j in range(len(game_board[:,0])):
              if game_board[j][i] == 1:
                  plt.scatter(i, j, s = 500, c = 'red', marker = 'o', edgecolors = 'black')
              if game_board[j][i] == 2:
                  plt.scatter(i, j, s = 500, c = 'blue', marker = 'o', edgecolors = 'black')
      
        
      #ax.set_yticklabels(ax.get_yticks(), rotation = 0)
      #ax.set_ylabels(['1', '2', '3', '4', '5', '6', '7'])
      #ax.set_xticklabels(ax.get_xticks(), rotation = 0)
      #ax.set_xlabels(['1', '2', '3', '4', '5', '6'])
      
      #col_number = ['1', '2', '3', '4', '5', '6', '7']
      #row_number = ['1', '2', '3', '4', '5', '6']
      
      #plt.xticks(game_board, col_number, xticks = None)
      #plt.yticks(game_board[:,0], row_number, yticks = None)
      
      plt.xlim(-.5, 6) 
      plt.ylim(-.5, 5)       
      plt.show()
      
      print ()
      print('Game Over! Thanks for playing.')
      print()
   
    else:
        if draw == True and win == False:
            print()
            print('Game is drawn. Thanks for playing.')
            print()
            
#print(bool(valid_col(game_board, input_col)))
#print(bool(next_open_row(game_board, input_col)))