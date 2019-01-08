class QueensPuzzle:

    def __init__(self, size):
        self.size = size
        self.solutions = 0
        self.simulate_puzzle()

    def simulate_puzzle(self):
        board = [-1] * self.size
        self.locate_queen(board, 0)
        self.print_result()

    def print_result(self):
        print("Found {} solutions for N = {}.".format(self.solutions, self.size))

    def locate_queen(self, board, current_row):
        if current_row == self.size:
            self.solutions += 1
        else:
            for column in range(self.size):
                if self.verify_spot(board, current_row, column):
                    board[current_row] = column
                    self.locate_queen(board, current_row + 1)

    @staticmethod
    def verify_spot(board, taken_rows, column):
        for row in range(taken_rows):
            if board[row] == column or \
                    board[row] - row == column - taken_rows or \
                    board[row] + row == column + taken_rows:
                return False
        return True

