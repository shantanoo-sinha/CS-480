# Write code to compute the answers to the questions below and print the answers.
# Feel free to modify this file and the other files as much as you like and need.
# Document your code if you'd like to receive any partial credit.
# Pay special attention to the formatting requirements.

# You probably want to start with importing classes and functions from the games file: from games import ...
from games import *
import global_var

first_move = "X"
X_count, O_count = 0, 0
X_data = []
O_data = []
board = {}
board1 = {}
vacant_count = 0

# Get the first line from the user. 
# An example input line: X - O
# In this example, the first entry is X, the second entry is -, indicating blank, and the third entry is O
print("Enter the first row.")
row1 = input().split()
index = 1
for val in row1:
    if val == "X":
        X_count += 1
        X_data.append(tuple((1, index)))
        board1[1, (index)] = val
    elif val == "O":
        O_count += 1
        O_data.append(tuple((1, index)))
        board1[1, (index)] = val
    else:
        board1[1, (index)] = index + 1
        vacant_count += 1
    index += 1
# print("X_count", X_count)
# print("O_count", O_count)

print("Enter the second row.")
row2 = input().split()
index = 1
for val in row2:
    if val == "X":
        X_count += 1
        X_data.append(tuple((2, index)))
        board1[2, (index)] = val
    elif val == "O":
        O_count += 1
        O_data.append(tuple((2, index)))
        board1[2, (index)] = val
    else:
        board1[2, (index)] = index + 10
        vacant_count += 1
    index += 1
# print("X_count", X_count)
# print("O_count", O_count)

print("Enter the third row.")
row3 = input().split()
index = 1
for val in row3:
    if val == "X":
        X_count += 1
        X_data.append(tuple((3, index)))
        board1[3, (index)] = val
    elif val == "O":
        O_count += 1
        O_data.append(tuple((3, index)))
        board1[3, (index)] = val
    else:
        board1[3, (index)] = index + 20
        vacant_count += 1
    index += 1
# print("X_count", X_count)
# print("O_count", O_count)

# print("X_data", X_data)
# print("O_data", O_data)

#my_state = GameState(
#    to_move = 'X',
#    utility = '',
#    board = {(1,1): x1.split()[0], (1,2): x1.split()[1], (1,3): x1.split()[2],
#             (2,1): x2.split()[0], (2,2): x2.split()[1], (2,3): x2.split()[2],
#             (3,1): x3.split()[0], (3,2): x3.split()[1], (3,3): x3.split()[2],
#            },
#    moves = []
#    )

def gen_state(to_move='X', x_positions=[], o_positions=[], h=3, v=3, k=3):
    """Given whose turn it is to move, the positions of X's on the board, the
    positions of O's on the board, and, (optionally) number of rows, columns
    and how many consecutive X's or O's required to win, return the corresponding
    game state"""
#     print("set", set([(x, y) for x in range(1, h + 1) for y in range(1, v + 1)]))
#     print("X set", set(x_positions))
#     print("O set", set(o_positions))
    
    moves = set([(x, y) for x in range(1, h + 1) for y in range(1, v + 1)]) \
            - set(x_positions) - set(o_positions)
    moves = list(moves)
#     print("moves", moves)
    moves.sort(key=lambda tup: (tup[0], tup[1]))
#     print("moves", moves)
#     board = {}
    for pos in x_positions:
        board[pos] = 'X'
    for pos in o_positions:
        board[pos] = 'O'
#     print("board:", board)
    return GameState(to_move=to_move, utility=0, board=board, moves=moves)


print("Whose turn is it now?")
# The answer should a single letter: either X or O. No punctuation. No other text.
if X_count > O_count:
    first_move = "O"
else:
    first_move = "X"
print(first_move)
print()

# Generating state
my_state = gen_state(to_move=first_move, x_positions=X_data, o_positions=O_data)


# Checking for initial terminal state
r1=(board1[(1,1)]==board1[(1,2)]==board1[(1,3)])
r2=(board1[(2,1)]==board1[(2,2)]==board1[(2,3)])
r3=(board1[(3,1)]==board1[(3,2)]==board1[(3,3)])
c1=(board1[(1,1)]==board1[(2,1)]==board1[(3,1)])
c2=(board1[(1,2)]==board1[(2,2)]==board1[(3,2)])
c3=(board1[(1,3)]==board1[(2,3)]==board1[(3,3)])
d1=(board1[(1,1)]==board1[(2,2)]==board1[(3,3)])
d2=(board1[(1,3)]==board1[(2,2)]==board1[(3,1)])
all_full = (vacant_count == 0)

# print(r1, r2, r3, c1, c2, c3, d1, d2, all_full)

winner=None
if r1==True:
    winner=board1[(1,1)]
elif r2==True:
    winner=board1[(2,1)]
elif r3==True:
    winner=board1[(3,1)]
elif c1==True:
    winner=board1[(1,1)]
elif c2==True:
    winner=board1[(1,2)]
elif c3==True:
    winner=board1[(1,3)]
elif d1==True:
    winner=board1[(1,1)]
elif d2==True:
    winner=board1[(1,3)]

terminal_state=(r1 or r2 or r3 or c1 or c2 or c3 or d1 or d2 or all_full)
terminal_utility=None

if terminal_state:
    if winner=='X':
        terminal_utility=1
    elif winner=='O':
        terminal_utility=-1
    else:
        terminal_utility=0

# print("terminal_state", terminal_state)
# print("winner", winner)
# print("terminal_utility", terminal_utility)


# For the following questions, you can implement everything here or under the questions or you can do a mix. 
# It's totally up to you where to put your implemention in this file.
# However, please pay special attention to the instructions regarding the format of the answers.


tttGame = TicTacToe()
# print("*********** Initial state ***********")
# tttGame.display(tttGame.initial)
# Setting initial state
tttGame.setState(my_state)
# print("*********** New state ***********")
# tttGame.display(my_state)
# tttGame.display(tttGame.initial)


print("How many states did the minimax algorithm evaluate?")
# The answer should a single number. No punctuation. No other text.
# You probably need to modify games.py to compute this.
if terminal_state:
    print(1)
else:
    minimax_decision(my_state, tttGame)
    print(global_var.minimax_states_evaluated)
    global_var.minimax_states_evaluated = 1
print()


print("How many states did the alpha-beta pruning algorithm evaluate?")
# The answer should a single number. No punctuation. No other text.
# You probably need to modify games.py to compute this.
if terminal_state:
    print(1)
else:
    alphabeta_search(my_state, tttGame)
    print(global_var.alphabeta_states_evaluated)
    global_var.alphabeta_states_evaluated = 1
print()


print("What is the value of the current state from the perspective of X?")
# The answer should a single number: either -1 or 1 or 0. No punctuation. No other text.
# Important: this is always from the perspective of X; *not* from the perspective of whose turn it is.
if terminal_state:
    print(terminal_utility)
else:
    print(global_var.utility_for_X)
print()


print("Assuming both X and O play optimally, does X have a guaranteed win? Is it a tie? Is it a guaranteed loss for X?")
# The answer should be either of "X will win.", or "It is a tie." or "X will lose."
# Note: you already computed this somewhere above.
if terminal_state:
    if winner=='X':
        X_result = "X will win."
    elif winner=='O':
        X_result = "X will lose."
    else:
        X_result = "It is a tie."
elif global_var.utility_for_X == 1:
    X_result = "X will win."
elif global_var.utility_for_X == -1:
    X_result = "X will lose."
else:
    X_result = "It is a tie."
print(X_result)
print()


print("Assuming both X and O would play optimally, how would they play till the game ends?")
# Display the states one at a time, using the display method of the Game class (or its subclasses, whichever is appropriate). 
# Print a single blank line between the states. That is, use print(). Do not print any additional info.
if terminal_state:
    tttGame.display(tttGame.initial)
else:
    tttGame.play_game(alphabeta_player, alphabeta_player)