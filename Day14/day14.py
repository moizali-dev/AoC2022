coords = []
import numpy as np
from board import Board
from arraygui import MyApp

file = "day14input.txt"

with open(file) as f:
    for lines in f:
        line = lines.rstrip()

        split_line = (line.split(" -> "))
        for s in split_line:
            xycoord = s.split(",")
            coords.append((int(xycoord[0]),int(xycoord[1])))

    print(coords)

max_x = 0
max_y = 0
min_x = 10000000

for coord in coords:
    if coord[0] > max_x:
        max_x = coord[0]
    if coord[1] > max_y:
        max_y = coord[1]
    if coord[0] < min_x:
        min_x = coord[0]


# Create board
print("\nMax Coord: ", (max_x, max_y),"Min Coord: ", (min_x, 0),"\n")

#### Part 1 ####
# board = Board(max_x,min_x,max_y, part=1)
    

# # Iterate through list from input
# coords = []
# with open(file) as f:
#     for lines in f:
#         line = lines.rstrip()

#         split_line = (line.split(" -> "))
#         for s in split_line:
#             xycoord = s.split(",")
#             coords.append((int(xycoord[0]),int(xycoord[1])))

#         for i in range(1,len(coords)):
#             coordsBoth = coords[i-1], coords[i]
        
#             # Adding to board
#             board.replaceInCoord(coordsBoth[0], coordsBoth[1])
#         coords = []


# board.printBoard()

# for i in range(10):
#     print(i)
#     board.SandFall()
#     print("--New Sand Falling--")
#     board.printBoard()

#### Part 2 ####
print("\n----PART 2----\n")
board = Board(max_x,min_x,max_y, part=2,additional_cols=1000)

# Iterate through list from input
coords = []
with open(file) as f:
    for lines in f:
        line = lines.rstrip()

        split_line = (line.split(" -> "))
        for s in split_line:
            xycoord = s.split(",")
            coords.append((int(xycoord[0]),int(xycoord[1])))

        for i in range(1,len(coords)):
            coordsBoth = coords[i-1], coords[i]
        
            # Adding to board
            board.replaceInCoord(coordsBoth[0], coordsBoth[1])
        coords = []

for i in range(100000):
    print(i)
    currEle = board.SandFall()
    print("--New Sand Falling--")
    if board.CheckTopRow() == True:
        break

print(i+1)