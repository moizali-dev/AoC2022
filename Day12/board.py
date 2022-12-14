class Board:

    def __init__(self, board, starting, ending) -> None:
        self.board = board
        self.starting = starting
        self.ending = ending

        self.curr_row = starting[0]
        self.curr_col = starting[1]
        self.end_dix = ending
        self.prev_idx = [0,0]
        self.prev_move = ""

    def getCurrElement(self):
        return self.board[self.curr_row][self.curr_col]

    def getCurrIdx(self):
        return self.curr_row, self.curr_col

    def getPrevElement(self):
        return self.board[self.prev_idx[0]][self.prev_idx[1]]

    def move(self,move):

        if move == "U":
            self.prev_idx = self.curr_row, self.curr_col
            self.curr_row -= 1
        if move == "D":
            self.prev_idx = self.curr_row, self.curr_col
            self.curr_row += 1
        if move == "R":
            self.prev_idx = self.curr_row, self.curr_col
            self.curr_col += 1
        if move == "L":
            self.prev_idx = self.curr_row, self.curr_col
            self.curr_col -= 1 

    def moveIdx(self, move):

        if move == "U":
            return self.curr_row - 1, self.curr_col
        if move == "D":
            return self.curr_row + 1, self.curr_col
        if move == "R":
            return self.curr_row, self.curr_col + 1
        if move == "L":
            return self.curr_row, self.curr_col - 1 

    def moveIsOOB(self, move):

        # move up
        if move == "U":
            if self.is_out_of_bounds(self.board, self.curr_row - 1, self.curr_col):
                return True
            else:
                return False

        # move down
        if move == "D":
            if self.is_out_of_bounds(self.board, self.curr_row + 1, self.curr_col):
                return True
            else:
                return False

        # move left
        if move == "L":
            if self.is_out_of_bounds(self.board, self.curr_row, self.curr_col - 1):
                return True
            else:
                return False

        # move right
        if move == "R":
            if self.is_out_of_bounds(self.board, self.curr_row, self.curr_col + 1):
                return True
            else:
                return False

    def is_out_of_bounds(self, arr, row, col):
        n = len(arr)
        m = len(arr[0])
        return row < 0 or row >= n or col < 0 or col >= m