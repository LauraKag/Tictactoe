# -*- coding: utf-8 -*-

#%%

board = [
['x', '0', 'x'],
['0', 'x', '0'],
['0', '0', '0']
]

def solved_horizontal(board):
    for row in board:
        if set(row) == set("x"):
            return True



def solved_vertical(board):
    for i in range(len(board)):
        count=0
        for j in range(len(board)):
            if board[j][i] == "x":
                count+=1
                if count == len(board):
                    return True


def solved_diagonal(board):
    count=0
    for i in range(len(board)):
        if board[i][i]=="x":
            count+=1
            if count == len(board):
                return True
    
    j=len(board)-1
    count=0
    for i in range(len(board)):
        if board[i][j] =="x":
            count+=1
            j-=1
            if count ==len(board):
                return True



