from orm.database import db_access, NCase, Solution


class QueensPuzzle:

    def __init__(self, size):
        self.size = size
        self.solutions = 0
        if db_access.query(NCase).filter_by(n=self.size).count() == 0:
            ncase = NCase(n=self.size, solutions=0)
            db_access.add(ncase)
            db_access.commit()
            self.ncase_id = ncase.id
            self.simulate_puzzle()
        else:
            ncase = db_access.query(NCase).filter_by(n=self.size).first()
            self.solutions = ncase.solutions
            self.print_result()

    def simulate_puzzle(self):
        board = [-1] * self.size
        self.locate_queen(board, 0)
        ncase = db_access.query(NCase).filter_by(n=self.size).first()
        ncase.solutions = self.solutions
        db_access.commit()
        self.print_result()

    def print_result(self):
        print("Found {} solutions for N = {}.".format(self.solutions, self.size))

    def locate_queen(self, board, current_row):
        if current_row == self.size:
            solution = Solution(ncase_id=self.ncase_id, solution=(str(board).strip('[]')).replace(" ", ""))
            db_access.add(solution)
            db_access.commit()
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

