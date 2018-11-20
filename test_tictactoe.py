# -*- coding: utf-8 -*-

#%%

import tictactoe

def test_tictactoe_horizontal_works():
    
    board = [[
    ['x', 'x', 'x'],
    ['x', 'x', '0'],
    ['x', '0', 'x']
    ],
    [['x','0', 'x'],
    ['x', 'x', 'x'],
    ['x', '0', 'x']
    ],
    [['x','0', 'x'],
    ['x', 'x', '0'],
    ['x', 'x', 'x']
    ]]

    for case in board:
        assert tictactoe.solved_horizontal(case)== True 
        

def test_tictactoe_vertical_works():
    
    board = [[
    ['x', '0', 'x'],
    ['x', '0', '0'],
    ['x', '0', 'x']
    ],
    [['0','x', 'x'],
    ['0', 'x', '0'],
    ['x', 'x', 'x']
    ],
    [['x','0', 'x'],
    ['0', 'x', 'x'],
    ['x', 'x', 'x']
    ]]
    
    for case in board:
        assert tictactoe.solved_vertical(case)== True 

def test_tictactoe_diagonal_works():
    
    board = [[
    ['x', '0', 'x'],
    ['0', 'x', '0'],
    ['0', '0', 'x']
    ],
    [['x','0', 'x'],
    ['0', 'x', '0'],
    ['x', 'x', '0']
    ]]
    
    for case in board:
        assert tictactoe.solved_diagonal(case)== True

def test_tictactoe_notwinning_works():
    
    board = [
    ['x', '0', 'x'],
    ['x', '0', '0'],
    ['0', '0', 'x']
    ]
    
    assert (tictactoe.solved_diagonal(board) == None and tictactoe.solved_horizontal(board) == None and tictactoe.solved_vertical(board) == None) == True
        
    