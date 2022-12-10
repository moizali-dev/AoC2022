import numpy as np
import math

from board import *
from utils import *

inputFile = "day9sampleinput.txt"

fns = functions()
num_tails = 10

start = "Bottom Left"

board_size = 11
HBoard = HeadBoard(board_size,board_size,"H",starting_point=start)
TTBoard = TailBoard(board_size, board_size,"*",starting_point=start)

def part1():

    TBoard = TailBoard(board_size, board_size,"T",starting_point=start)

    with open(inputFile) as f:
        for lines in f:
            line_input = lines.rstrip()

            move = line_input[0]
            times = line_input[1:]

            for t in range(int(times)):
                # curr_row_head, curr_col_head = moveHeadBoard(curr_row_head,curr_col_head,move,HeadBoard)
                HBoard.moveHeadBoard(move)
                # HBoard.PrintCleanBoard()
                
                if fns.isAdjacent(HBoard.curr_row,HBoard.curr_col, TBoard.curr_row, TBoard.curr_col) == False:
                    unit_vector = fns.unitVector(HBoard.curr_row,HBoard.curr_col, TBoard.curr_row, TBoard.curr_col)
                    # print(unit_vector)
                    # move Tails
                    TBoard.moveTailBoard(unit_vector)
                    
                    # Tracking in TailTrackBoard
                    TTBoard.setElement(TBoard.getRowsCols()[0], TBoard.getRowsCols()[1], "*")
                    # TBoard.PrintCleanBoard()

                # fns.PrintCleanBoard(HBoard, TBoard)


    # TTBoard.PrintCleanBoard()
    return fns.countTailTracks(TTBoard)

def part2():

    TBoardLst = []
    for i in range(1,num_tails):
        TBoardLst.append(TailBoard(board_size,board_size,i,starting_point=start))

    with open(inputFile) as f:
        for lines in f:
            line_input = lines.rstrip()

            move = line_input[0]
            times = line_input[1:]

            for t in range(int(times)):
                # curr_row_head, curr_col_head = moveHeadBoard(curr_row_head,curr_col_head,move,HeadBoard)
                HBoard.moveHeadBoard(move)
                # HBoard.PrintCleanBoard()

                for TBoard in TBoardLst:
                
                    # Run for the first Tail
                    if TBoard.getType() == 1:
                        if fns.isAdjacent(HBoard.curr_row,HBoard.curr_col, TBoard.curr_row, TBoard.curr_col) == False:
                            unit_vector = fns.unitVector(HBoard.curr_row,HBoard.curr_col, TBoard.curr_row, TBoard.curr_col)
                            # print(unit_vector)
                            # move Tails
                            TBoard.moveTailBoard(unit_vector)
                        prevTBoard = TBoard

                    else: # run for subsequent tails
                        if fns.isAdjacent(prevTBoard.curr_row,prevTBoard.curr_col, TBoard.curr_row, TBoard.curr_col) == False:
                            unit_vector = fns.unitVector(prevTBoard.curr_row,prevTBoard.curr_col, TBoard.curr_row, TBoard.curr_col)
                            # print(unit_vector)
                            # move Tails
                            TBoard.moveTailBoard(unit_vector)
                        prevTBoard = TBoard
                        
                # Tracking in TailTrackBoard
                TTBoard.setElement(TBoard.getRowsCols()[0], TBoard.getRowsCols()[1], "*")
                    
                # HBoard.PrintCleanBoard()
                # for TBoard in TBoardLst:
                #     TBoard.PrintCleanBoard()
                fns.PrintCleanBoardManyTails(HBoard, TBoardLst)

                # fns.PrintCleanBoard(HBoard, TBoard)


    return fns.countTailTracks(TTBoard)

if __name__ == "__main__":

    print(f'Solution for Part1: {part1()}')
    print(f'Solution for Part2: {part2()}')
