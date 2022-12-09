import numpy as np
import math

inputFile = "day9input.txt"

arr_rows = 500
arr_cols = 500

HeadBoard = np.chararray((arr_rows, arr_cols), unicode=True)
TailBoard = np.chararray((arr_rows, arr_cols), unicode=True)
TailTrackBoard = np.chararray((arr_rows, arr_cols), unicode=True)

HeadBoard[:] = '.'
TailBoard[:] = '.'
TailTrackBoard[:] = '.'

curr_row_head = curr_row_tail = arr_rows // 2
curr_col_head = curr_col_tail = arr_cols // 2

HeadBoard[arr_rows // 2][arr_cols // 2] = 'H'
TailBoard[arr_rows // 2][arr_cols // 2] = 'T'
TailTrackBoard[arr_rows // 2][arr_cols // 2] = "*"

def moveHeadBoard(curr_row, curr_col, move, arr):

    # move up
    if move == "U":
        arr[curr_row - 1][curr_col] = "H"
        arr[curr_row][curr_col] = "."
        return curr_row - 1, curr_col

    # move down
    if move == "D":
        arr[curr_row + 1][curr_col] = "H"
        arr[curr_row][curr_col] = "."
        return curr_row + 1, curr_col

    # move left
    if move == "L":
        arr[curr_row][curr_col - 1] = "H"
        arr[curr_row][curr_col] = "."
        return curr_row, curr_col - 1

    # move right
    if move == "R":
        arr[curr_row][curr_col + 1] = "H"
        arr[curr_row][curr_col] = "."
        return curr_row, curr_col + 1


def isAdjacent(i, j, x, y):

    # Check if Head is next to Tails
    if x == i - 1 and y == j:  
        return True
    elif x == i + 1 and y == j: 
        return True
    elif x == i and y == j - 1: 
        return True
    elif x == i and y == j + 1: 
        return True
    elif x == i - 1 and y == j - 1:  
        return True
    elif x == i - 1 and y == j + 1:  
        return True
    elif x == i + 1 and y == j - 1:  
        return True
    elif x == i + 1 and y == j + 1:  
        return True
    else:
        return False

def unitVector(i, j, x, y):
    # calculate the direction vector
    v = (x - i, y - j)

    # calculate the magnitude of v
    magnitude = math.sqrt(v[0] ** 2 + v[1] ** 2)

    # calculate the unit vector in the direction of v
    if magnitude != 0:
        unit_vector = [v[0] / magnitude, v[1] / magnitude]
    else:
        unit_vector = [0,0]

    # print the result
    return unit_vector

def moveTailBoard(curr_row, curr_col, unitvector, arr):

    # move up
    if unitvector[0] > 0 and unitvector[1] == 0: # e.g. [1.0, 0.0]
        arr[curr_row - 1][curr_col] = "T"
        arr[curr_row][curr_col] = "."
        return curr_row - 1, curr_col

    # # move down
    if unitvector[0] < 0 and unitvector[1] == 0: # e.g. [-1.0, 0.0]
        arr[curr_row + 1][curr_col] = "T"
        arr[curr_row][curr_col] = "."
        return curr_row + 1, curr_col

    # move down right
    if unitvector[0] < 0 and unitvector[1] < 0: # e.g. [-0.4472135954999579, -0.8944271909999159]
        arr[curr_row + 1][curr_col + 1] = "T"
        arr[curr_row][curr_col] = "."
        return curr_row + 1, curr_col + 1

    # move down left
    if unitvector[0] < 0 and unitvector[1] > 0: # e.g. [-0.4472135954999579, 0.8944271909999159]
        arr[curr_row + 1][curr_col - 1] = "T"
        arr[curr_row][curr_col] = "."
        return curr_row + 1, curr_col - 1


    # move left
    if unitvector[0] == 0 and unitvector[1] > 0: # e.g. [0.0, 1.0]
        arr[curr_row][curr_col - 1] = "T"
        arr[curr_row][curr_col] = "."
        return curr_row, curr_col - 1

    # move up left
    if unitvector[0] > 0 and unitvector[1] > 0: # e.g. [0.4472135954999579, 0.8944271909999159]
        arr[curr_row - 1][curr_col - 1] = "T"
        arr[curr_row][curr_col] = "."
        return curr_row - 1, curr_col - 1

    # move right
    if unitvector[0] == 0 and unitvector[1] < 0: # e.g. (0.0, -1.0)
        arr[curr_row][curr_col + 1] = "T"
        arr[curr_row][curr_col] = "."
        return curr_row, curr_col + 1

    # move up right
    if unitvector[0] > 0 and unitvector[1] < 0: # e.g. [0.8944271909999159, -0.4472135954999579]
        arr[curr_row - 1][curr_col + 1] = "T"
        arr[curr_row][curr_col] = "."
        return curr_row - 1, curr_col + 1

    if unitvector[0] == 0 and unitvector[1] == 0:
        return curr_row, curr_col

def PrintCleanBoard(HeadBoard, TailBoard):

    rows = len(HeadBoard)
    cols = len(HeadBoard[0])

    for r in range(rows):
        for c in range(cols):

            if HeadBoard[r][c] == '.' and TailBoard[r][c] == '.':
                print(".", end = ' ')
            elif HeadBoard[r][c] == 'H' and TailBoard[r][c] == '.':
                print("H", end = ' ')
            elif HeadBoard[r][c] == '.' and TailBoard[r][c] == 'T':
                print("T", end = ' ')
            elif HeadBoard[r][c] == 'H' and TailBoard[r][c] == 'T':
                print("B", end = ' ')

        print() 

def countTailTracks(TrailTrackBoard):

    rows = len(TrailTrackBoard)
    cols = len(TrailTrackBoard[0])

    count = 0

    for r in range(rows):
        for c in range(cols):
            if TrailTrackBoard[r][c] == "*":
                count += 1

    return count


with open(inputFile) as f:
    for lines in f:
        line_input = lines.rstrip()

        move = line_input[0]
        times = line_input[1:]

        print(move, times)
        for t in range(int(times)):
            curr_row_head, curr_col_head = moveHeadBoard(curr_row_head,curr_col_head,move,HeadBoard)
            # print(curr_row_head, curr_col_head)
            # print(HeadBoard)
            
            if isAdjacent(curr_row_head,curr_col_head, curr_row_tail, curr_col_tail) == False:
                unit_vector = unitVector(curr_row_head,curr_col_head, curr_row_tail, curr_col_tail)
                # print(unit_vector)
                # move Tails
                curr_row_tail, curr_col_tail = moveTailBoard(curr_row_tail,curr_col_tail,unit_vector,TailBoard)
                
                # Tracking in TailTrackBoard
                TailTrackBoard[curr_row_tail][curr_col_tail] = "*"

            # print(TailBoard)
            # PrintCleanBoard(HeadBoard, TailBoard)

# print(TailTrackBoard)
print(countTailTracks(TailTrackBoard))
