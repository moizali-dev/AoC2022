import numpy as np

class Board:

    def __init__(self, rows, cols, type, starting_point = "Middle") -> None:
        self.rows = rows
        self.cols = cols
        self.type = type

        self.board = np.chararray((self.rows, self.cols), unicode=True)
        self.board[:] = '.'

        if starting_point == "Middle":
            self.curr_row = self.rows // 2
            self.curr_col = self.cols // 2
        elif starting_point == "Bottom Left":
            self.curr_row = self.rows - 1
            self.curr_col = 0

        self.board[self.curr_row][self.curr_col] = self.type

    def getRows(self):
        return self.rows

    def getCols(self):
        return self.cols

    def getType(self):
        return self.type

    def getRowsCols(self):
        return self.curr_row, self.curr_col

    def setElement(self, row, col, setvalue):
        self.board[row][col] = setvalue

    def getElement(self, row, col):
        return self.board[row][col]

    def PrintCleanBoard(self):

        print("---PRINTING BOARD---")

        for r in range(self.rows):
            for c in range(self.cols):
                print(self.board[r][c], end = ' ')
            print() 

class HeadBoard(Board):

    def __init__(self, rows, cols, type, starting_point="Middle") -> None:
        super().__init__(rows, cols, type, starting_point)

    def moveHeadBoard(self, move):

        # move up
        if move == "U":
            self.board[self.curr_row - 1][self.curr_col] = self.type
            self.board[self.curr_row][self.curr_col] = "."

            self.curr_row = self.curr_row - 1

        # move down
        if move == "D":
            self.board[self.curr_row + 1][self.curr_col] = self.type
            self.board[self.curr_row][self.curr_col] = "."
            
            self.curr_row = self.curr_row + 1

        # move left
        if move == "L":
            self.board[self.curr_row][self.curr_col - 1] = self.type
            self.board[self.curr_row][self.curr_col] = "."
            
            self.curr_col = self.curr_col - 1

        # move right
        if move == "R":
            self.board[self.curr_row][self.curr_col + 1] = self.type
            self.board[self.curr_row][self.curr_col] = "."

            self.curr_col = self.curr_col + 1


class TailBoard(Board):

    def __init__(self, rows, cols, type, starting_point="Middle") -> None:
        super().__init__(rows, cols, type, starting_point)

    def getRows(self):
        return super().getRows()

    def getCols(self):
        return super().getCols()

    def getRowsCols(self):
        return super().getRowsCols()

    def getType(self):
        return super().getType()

    def setElement(self, row, col, setvalue):
        return super().setElement(row, col, setvalue)

    def getElement(self, row, col):
        return super().getElement(row, col)

    def moveTailBoard(self, unitvector):

        # move up
        if unitvector[0] > 0 and unitvector[1] == 0: # e.g. [1.0, 0.0]
            self.board[self.curr_row - 1][self.curr_col] = self.type
            self.board[self.curr_row][self.curr_col] = "."
            
            self.curr_row = self.curr_row - 1

        # # move down
        if unitvector[0] < 0 and unitvector[1] == 0: # e.g. [-1.0, 0.0]
            self.board[self.curr_row + 1][self.curr_col] = self.type
            self.board[self.curr_row][self.curr_col] = "."
            
            self.curr_row = self.curr_row + 1

        # move down right
        if unitvector[0] < 0 and unitvector[1] < 0: # e.g. [-0.4472135954999579, -0.8944271909999159]
            self.board[self.curr_row + 1][self.curr_col + 1] = self.type
            self.board[self.curr_row][self.curr_col] = "."
            
            self.curr_row = self.curr_row + 1
            self.curr_col = self.curr_col + 1

        # move down left
        if unitvector[0] < 0 and unitvector[1] > 0: # e.g. [-0.4472135954999579, 0.8944271909999159]
            self.board[self.curr_row + 1][self.curr_col - 1] = self.type
            self.board[self.curr_row][self.curr_col] = "."
            
            self.curr_row = self.curr_row + 1
            self.curr_col = self.curr_col - 1


        # move left
        if unitvector[0] == 0 and unitvector[1] > 0: # e.g. [0.0, 1.0]
            self.board[self.curr_row][self.curr_col - 1] = self.type
            self.board[self.curr_row][self.curr_col] = "."
            
            self.curr_col = self.curr_col - 1

        # move up left
        if unitvector[0] > 0 and unitvector[1] > 0: # e.g. [0.4472135954999579, 0.8944271909999159]
            self.board[self.curr_row - 1][self.curr_col - 1] = self.type
            self.board[self.curr_row][self.curr_col] = "."
            
            self.curr_row = self.curr_row - 1
            self.curr_col = self.curr_col - 1

        # move right
        if unitvector[0] == 0 and unitvector[1] < 0: # e.g. (0.0, -1.0)
            self.board[self.curr_row][self.curr_col + 1] = self.type
            self.board[self.curr_row][self.curr_col] = "."
            
            self.curr_col = self.curr_col + 1

        # move up right
        if unitvector[0] > 0 and unitvector[1] < 0: # e.g. [0.8944271909999159, -0.4472135954999579]
            self.board[self.curr_row - 1][self.curr_col + 1] = self.type
            self.board[self.curr_row][self.curr_col] = "."
            
            self.curr_row = self.curr_row - 1
            self.curr_col = self.curr_col + 1

        if unitvector[0] == 0 and unitvector[1] == 0:
            pass

# if __name__ == "__main__": 

#     Hbrd = HeadBoard(6,6,"H")
#     Hbrd.PrintCleanBoard()
#     Hbrd.moveHeadBoard("R")
#     Hbrd.PrintCleanBoard()





    

        