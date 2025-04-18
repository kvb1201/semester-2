# Consider the 8 queen's problem, it is a 8*8 chess board where you need to place queens
# according to the following constraints.
# a. Each row should have exactly only one queen.
# b. Each column should have exactly only one queen.
# c. No queens are attacking each other.
# Write a program to place the queens randomly in the chess board so that all the conditions
# are satisfied. Find the solutions to the problem.

import numpy as np
import random 

def isSafe(board,row,col):
    if 1 in board[row]: #check for row
        return False
    for i in range(8): #check for column
        if board[i][col] == 1:
            return False
    i,j=row,col # check for left diagonal
    while(i>=0 and j >=0):
        if(board[i][j] == 1):
            return False
        i-=1
        j-=1
    i,j = row,col #check for right diagonal
    while(i>=0 and j <8):
        if(board[i][j] == 1):
            return False
        i -=1
        j+=1
    return True

def nQueens(board, row):
    if(row == 8):
        return True
    cols = list(range(8))
    random.shuffle(cols)

    for col in cols:
        if isSafe(board,row,col):
            board[row][col] = 1
            if nQueens(board,row+1):
                return True
            board[row][col]=0

    return False

        

board = np.zeros((8,8),dtype=int)
if nQueens(board,0):
    print(board)

    
    








