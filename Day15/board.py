import numpy as np
from scipy import sparse
from typing import Tuple
from tqdm import tqdm

class Board:

    def __init__(self, min_x, min_y, max_x, max_y) -> None:

        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

        self.rows = max_y + min_y + 1
        self.cols = max_x - min_x + 1
        
        self.board = np.zeros((self.rows,self.cols), dtype=int)
        # self.board[:] = 0

    def getElement(self, coord):

        coord = self._transposeCoord(coord)
        return self.board[coord[1]][coord[0]]

    def updateBoard(self, coord:Tuple, updatedEle:int):

        updatedCoord = self._transposeCoord(coord)
        self.board[updatedCoord[1], updatedCoord[0]] = updatedEle

    def getRow(self, rownum):
        rownum = rownum + self.min_y
        return self.board[rownum]

    def sensorBeaconScan(self, sensorCoord, beaconCoord):

        mh = self._ManhattanDistance(sensorCoord, beaconCoord)
        
        # Create new board to map the beacon
        # distanceBoard = copy.deepcopy(self.board)

        for i in tqdm(range(len(self.board))):
            for j in range(len(self.board[i])):
    
                compareCoord = self._transposeCoord((j,i),reverese=True)
                calcMH = self._ManhattanDistance(sensorCoord, compareCoord)
    
                if calcMH <= mh:
                    if self.board[i][j] == 0:
                        self.board[i][j] = 3

        # for i in range(len(distanceBoard)):
        #     for j in range(len(distanceBoard[i])):
        #         print(distanceBoard[i][j], end="")
        #     print()

        # Replace # in self.board where an element in distanceBoard has one
        # for i in range(len(self.board)):
        #     for j in range(len(self.board[i])):
        #         if distanceBoard[i][j] == 3:
        #             self.board[i][j] = 3

    def sensorBeaconScanRow(self, sensorCoord, beaconCoord, row):

        mh = self._ManhattanDistance(sensorCoord, beaconCoord)
        rownum = row + self.min_y

        for i in range(self.cols):
            # print(rownum,i, self.board[rownum][i])
            compareCoord = self._transposeCoord((i,row),reverese=True)
            calcMH = self._ManhattanDistance(sensorCoord, compareCoord)

            if calcMH <= mh:
                if self.board[rownum][i] == 0:
                    self.board[rownum][i] = 3
    
    def OOB(self, coord):

        col, row = self._transposeCoord(coord)
        print(col, row, self.cols, self.rows)
        if row < 0 or row > (self.rows - 1):
            return True
        if col < 0 or col > (self.cols - 1):
            return True
        return False


    def _ManhattanDistance(self, coord1, coord2):

        # | x1 - x2 | + | y1 - y2 |
        coord1 = self._transposeCoord(coord1)
        coord2 = self._transposeCoord(coord2)

        return (abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1]))

    def _transposeCoord(self, coord:Tuple, reverese=False)->Tuple:
        
        x = coord[0]
        y = coord[1]

        if reverese == False:
            x = x - self.min_x
            y = y - self.min_y
        elif reverese == True:
            x = x + self.min_x
            y = y + self.min_y

        return (x,y)


    def printBoard(self):
        # Iterate through the rows of the matrix
        for row in self.board:
            # Iterate through the elements in the current row
            for element in row:
                # Print the current element
                print(element, end="")
                # Add a newline after each row
            print()