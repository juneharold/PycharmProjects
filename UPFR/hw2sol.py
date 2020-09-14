# Ex 1
import numpy as np
import random

def create_board():
    board = np.zeros((3,3), dtype = int)
    return board
board = create_board()
# Ex 2
def create_board():
    board = np.zeros((3,3),dtype=int)
    return board
board = create_board()

def place(board,player,position):
    if board[position] == 0:
        board[position] = player
        return board
place(board,1,(0,0))
# Ex 3
def possibilities(board):
    return list(zip(*np.where(board == 0)))

possibilities(board)
# Ex 4
# write your code here!
def random_place(board, player):
    possible_placements = possibilities(board)
    if len(possible_placements) > 0:
        possible_placements = random.choice(possible_placements)
        place(board, player, possible_placements)
    return board

random_place(board, 2)
# Ex 5
board = create_board()
for i in range(3):
    for player in [1, 2]:
       random_place(board, player)
print(board)
# Ex 6
def row_win(board,player):
    winner = False
    if np.any(np.all(board==player,axis=1)):
        return True
    else:
        return False

row_win(board, 1)
# Ex 7
def col_win(board,player):
    if np.any(np.all(board == player, axis = 0)):
        return True
    else:
        return False
col_win(board,1)
# Ex 8
def diag_win(board, player):
    if np.all(np.diag(board)==player):
        return True
    else:
        return False
diag_win(board, 1)
# Ex 9
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply.  if so, store `player` as `winner`.
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner
evaluate(board)
# Ex 10
# write your code here!
def play_game():
    board,winner = create_board(),0
    while winner == 0:
        for player in [1,2]:
            random_place(board,player)
            winner = evaluate(board)
            if winner !=0:
                break
    return winner
# Ex 11
random.seed(1)
games = [play_game() for i in range(1000)]
"""print(games.count(1))
print(games.count(2))
print(games.count(0))
print(games.count(3))"""
# Ex 12
def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            # use `random_place` to play a game, and store as `board`.
            random_place(board,player)
            winner = evaluate(board)
            # use `evaluate(board)`, and store as `winner`.
            if winner != 0:
                break
    return winner

play_strategic_game()
# Ex 13
games = [play_strategic_game() for i in range(1000)]
games.count(1)
print(games.count(1))
print(games.count(2))
print(games.count(0))
print(games.count(3))







