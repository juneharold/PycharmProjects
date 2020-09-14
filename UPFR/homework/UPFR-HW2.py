import numpy as np
import random


def create_board():
    return np.zeros((3, 3), dtype=int)

board = create_board()


def place(board, player, position):
    if player == 1:
        board[position] = 1
    elif player == 2:
        board[position] = 2


place(board, 1, (0, 0))

print(board)


def possibilities(board):
    empty_position = np.where(board == 0)
    list = []
    for i in range(len(empty_position[0])):
        list.append((empty_position[0][i], empty_position[1][i]))
    return list


"""print(possibilities(board))"""


def random_place(board, player):
    ep = random.choice(possibilities(board))
    board[ep] = player
    return board


"""random_place(board, 1)
random_place(board, 2)
random_place(board, 1)
random_place(board, 2)
random_place(board, 1)
random_place(board, 2)"""


def row_win(board, player):
    for i in range(2):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        else:
            return False


print(row_win(board, 1))


def col_win(board, player):
    for i in range(2):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
        else:
            return False


print(col_win(board, 1))

board[1, 1] = 2


# write your code here!
def diag_win(board, player):
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == player:
        return True
    else:
        return False


print(diag_win(board, 2))


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # add your code here!
        if row_win(board, player) is True:
            winner = player
        elif col_win(board, player) is True:
            winner = player
        elif diag_win(board, player) is True:
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


print(evaluate(board))


# write your code here!
def play_game():
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

play_game()



random.seed(1)
results = []
for i in range(1000):
    r = play_game()
    results.append(r)

print(results.count(1))


"""def p_g():
    board = create_board()
    board[1][1] = 1
    winner = 0
    while winner == 0:
        for player in [2, 1]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner


def play_strategic_game():
    board = create_board()
    board[1][1] = 1
    winner = 0
    while winner == 0:
        for player in [2, 1]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner


ot = []
for i in range(1000):
    ot.append(play_strategic_game())

print(ot.count(1))"""


