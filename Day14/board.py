import numpy as np
from time import sleep

class Board:

    def __init__(self, max_x, min_x, max_y,min_y = 0, part = 1, additional_cols = 0) -> None:
        self.min_x = min_x
        self.addition_cols = additional_cols

        if part == 1:
            self.rows = max_y + 1
            self.cols = max_x - min_x + 1

            rows = max_y + 1
            cols = max_x - min_x + 1
        
            self.board = np.chararray((rows, cols), unicode=True)
            self.board[:] = '.'

        elif part == 2:
            self.rows = max_y + 1 + 2
            self.cols = max_x - min_x + 1

            rows = max_y + 1 + 2
            cols = max_x - min_x + 1

            self.board = np.chararray((rows, cols), unicode=True)
            self.board[:] = '.'

            arrToAppend = np.chararray((rows, 1), unicode=True)
            arrToAppend[:] = '.'
            
            # append to right
            for i in range(additional_cols):
                self.board = np.column_stack((arrToAppend, self.board))
                self.cols += 1

            for i in range(self.cols):
                self.board[rows - 1][i] = "#"

    def getBoard(self):
        return self.board

    def CheckTopRow(self):
        # Get the first row of the matrix
        first_row = self.board[0, :]

        # Iterate over the elements in the first row
        for ele in first_row:
            if ele == "+":
                return True

        return False
        

    def replaceInCoord(self, coord1, coord2):
    
        # Move Vertical
        if coord1[0] == coord2[0]:
            x = coord1[0] - self.min_x + self.addition_cols // 2
            
            if coord1[1] > coord2[1]:
                rangeStart = coord2[1]
                rangeEnd = coord1[1] + 1
            else:
                rangeStart = coord1[1]
                rangeEnd = coord2[1] + 1

            for y in range(rangeStart, rangeEnd):
                self.board[y,x] = "#"

        # Move Horizontal
        elif coord1[1] == coord2[1]:

            y = coord1[1]

            x1 = coord1[0] - self.min_x + self.addition_cols // 2
            x2 = coord2[0] - self.min_x + self.addition_cols // 2
            if x1 > x2:
                rangeStart = x2
                rangeEnd = x1 + 1
            else:
                rangeStart = x1
                rangeEnd = x2 + 1

            for x in range(rangeStart, rangeEnd):
                self.board[y,x] = "#"
            

    def printBoard(self):
        # Iterate through the rows of the matrix
        for row in self.board:
            # Iterate through the elements in the current row
            for element in row:
                # Print the current element
                print(element, end=" ")
                # Add a newline after each row
            print()

    def countHash(self):
        count = 0
        # Iterate through the rows of the matrix
        for row in self.board:
            # Iterate through the elements in the current row
            for element in row:
                # Print the current element
                if element == "#":
                    count += 1

        return count

    def updateBottom(self, currcoord)->bool:

        if self.board[currcoord[0] + 1, currcoord[1]] != "#" and self.board[currcoord[0] + 1, currcoord[1]] != "+":
            self.board[self.currcoord[0],self.currcoord[1]] = "."
            self.currcoord = (self.currcoord[0] + 1, self.currcoord[1])
            self.board[self.currcoord[0],self.currcoord[1]] = "+"
            return True
        else:
            return False

    def updateBottomLeft(self, currcoord)->bool:
        if self.board[currcoord[0] + 1, currcoord[1] - 1] != "#" and self.board[currcoord[0] + 1, currcoord[1] - 1] != "+":
            self.board[self.currcoord[0],self.currcoord[1]] = "."
            self.currcoord = (self.currcoord[0] + 1, self.currcoord[1] - 1)
            self.board[self.currcoord[0],self.currcoord[1]] = "+"
            return True
        else:
            return False

    def updateBottomRight(self, currcoord)->bool:
        if self.board[currcoord[0] + 1, currcoord[1] + 1] != "#" and self.board[currcoord[0] + 1, currcoord[1] + 1] != "+":
            self.board[self.currcoord[0],self.currcoord[1]] = "."
            self.currcoord = (self.currcoord[0] + 1, self.currcoord[1] + 1)
            self.board[self.currcoord[0],self.currcoord[1]] = "+"
            return True
        else:
            return False

    def SandFall(self):

        startingcoord = (500 - self.min_x + (self.addition_cols // 2), 0)
        self.currcoord = (startingcoord[1], startingcoord[0])
        self.board[self.currcoord[0],self.currcoord[1]] = "+"

        condition = False
        while condition == False:
            # self.printBoard()
            # sleep(0.5)
            # Check update down
            if self.updateBottom(self.currcoord) == False:
                
                # Check update left
                if self.updateBottomLeft(self.currcoord) == False:

                    # Check update right
                    if self.updateBottomRight(self.currcoord) == False:
                        condition = True


