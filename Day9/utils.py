from typing import List
import math

from board import *

class functions:

    def __init__(self) -> None:
        pass

    def isAdjacent(self, i, j, x, y):

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

    def unitVector(self, i, j, x, y):
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

    def PrintCleanBoard(self, HeadBoardInput, TailBoardInput):

        rows = HeadBoardInput.rows
        cols = HeadBoardInput.cols

        for r in range(rows):
            for c in range(cols):

                if HeadBoardInput[r][c] == '.' and TailBoardInput[r][c] == '.':
                    print(".", end = ' ')
                elif HeadBoardInput[r][c] == 'H' and TailBoardInput[r][c] == '.':
                    print("H", end = ' ')
                elif HeadBoardInput[r][c] == '.' and TailBoardInput[r][c] == 'T':
                    print("T", end = ' ')
                elif HeadBoardInput[r][c] == 'H' and TailBoardInput[r][c] == 'T':
                    print("B", end = ' ')

            print() 

    def PrintCleanBoardManyTails(self, HBoardInput:HeadBoard, TailBoardList:List[TailBoard]):

        print("--PRINTING NEW BOARD--")

        rows = HBoardInput.getRows()
        cols = HBoardInput.getCols()

        for r in range(rows):
            for c in range(cols):

                # H overrides
                if HBoardInput.getElement(r,c) == "H":
                    print("H", end = ' ')
                
                elif HBoardInput.getElement(r,c) != "H":
                    tail_lst = []
                    for TailBoard in TailBoardList:
                        if TailBoard.getElement(r,c) != ".":
                            tail_lst.append(int(TailBoard.getElement(r,c)))
                    #Check minium of tail_lst
                    if len(tail_lst) > 0:
                        print(str(min(tail_lst)), end = ' ')
                    else:
                        print(".", end=' ')
                else:
                    print(".", end = ' ')
            print() 


    def countTailTracks(self, TrailTrackBoard:TailBoard):

        rows = TrailTrackBoard.getRows()
        cols = TrailTrackBoard.getCols()

        count = 0

        # print(TrailTrackBoard[0][0]) why cant this be used???
        for r in range(rows):
            for c in range(cols):
                if TrailTrackBoard.getElement(r,c) == "*":
                    count += 1

        return count


