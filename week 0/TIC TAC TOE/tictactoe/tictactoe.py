"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countx = 0
    counto = 0

    for row in range(len(board)):
        for col in range(len(row)):
            if board[row][col] == X:
                countx += 1
            if board[row][col]  == 0:
                counto += 1
    if countx > counto :
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allPossibleActions = set()
    for row in range(len(board)):
        for col in range(len(row)):
            if board[row][col] == EMPTY:
                allPossibleActions.add((row,col))
    
    return allPossibleActions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not Valid Action")
    
    row, col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
    return board_copy


def checkRow(board,player):
    for row in range(len(board)):
        if board[row][0] == player(board) and board[row][1] == player(board) and board[row][2] == player(board):
            return True
    return False

def checkCol(board,player):
    for col in range(len(board)):
        if board[0][col] == player(board) and board[1][col] == player(board) and board[2][col] == player(board):
            return True
    return False

def checkFirstDiagonal(board,player):
    count = 0
    for row in range(len(board)):
        for col in range(len(row)):
            if row == col and board[row][col] == player(board):
                count +=1
    if count == 3:
        return True
    else:
        return False
    
def checkSecondDiagonal(board,player):
    count = 0
    for row in range(len(board)):
        for col in range(len(row)):
            if col == (len(board) - row -1) and board[row][col] == player(board):
                count +=1
    if count == 3:
        return True
    else:
        return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRow(board, X) or checkCol(board, X) or checkFirstDiagonal(board, X) or checkSecondDiagonal(board, X):
        return X
    elif checkRow(board, O) or checkCol(board, O) or checkFirstDiagonal(board, O) or checkSecondDiagonal(board, O):
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
