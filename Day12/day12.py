import numpy as np

from board import Board
row = 0

with open("/Users/moizali/Documents/Personal/AoC2022/Day12/day12sampleinput.txt") as f:
    for lines in f:
        line = lines.rstrip()

        # Find S
        if 'S' in line:
            S = [row, line.find('S')]

        # Find E
        if 'E' in line:
            E = [row, line.find('E')]

        if row == 0:
            arr = np.array([list(line)])
        else: 
            arr = np.vstack([arr, np.array(list(line))])
        row += 1


print(arr)

# initializing board
myBoard = Board(arr,S,E)
moves = ["U", "D", "L", "R"]

def condition_to_continue(board):

    print(board.getCurrElement(), board.getPrevElement())
    if ord(board.getCurrElement()) - ord(board.getPrevElement()) == 1:
        return True 
    elif ord(board.getCurrElement()) - ord(board.getPrevElement()) == 0:
        return True
    elif board.getCurrElement() == "S" or board.getPrevElement() == "S":
        return True
    else:
        return False

prev_move_dict = {"U":"D", "D":"U","L":"R", "R":"L"}

def is_out_of_bounds(self, arr, row, col):
    n = len(arr)
    m = len(arr[0])
    return row < 0 or row >= n or col < 0 or col >= m

# recursion solution
def find_min_path(board, lst = [], path = "", visited_elements = [], prev_move = ""):

    visited_elements.append(board.getCurrIdx())

    if board.getCurrElement() == "S":
        path = ""
    else:
        path += board.getCurrElement()

    # base case
    if path in lst:
        return

    if condition_to_continue(board) == False:
        lst.append(path)
        return 

    print(path)

    # recursively try
    for m in moves:
        if m == prev_move:
            pass
        elif board.moveIsOOB(m):
            pass
        elif board.moveIdx(m) in visited_elements:
            pass
        else:
            board.move(m)
            prev_move = prev_move_dict[m]
            find_min_path(board, lst, path, visited_elements, prev_move)

print(find_min_path(myBoard))
