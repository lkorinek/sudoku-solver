class Solver:
    """
    Backtracking solver for sudoku
    """

    def __init__(self, board):

        self.board = board
        self.size = len(self.board)
        self.steps = []

    def __str__(self):
        """
        Return human readable state
        """

        result = ""
        for i in range(self.size):
            if i != 0 and i % 3 == 0:
                result += "---------------------\n"

            for j in range(self.size):
                if j != 0 and j % 3 == 0:
                    result += "| "
                result += str(self.board[i][j]) + " "
            result += "\n"

        return result

    def find_empty(self):
        """
        Find an empty position on the board
        return variables
        """

        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j

    def validate(self, pos, num):
        """
        Validate if it is possible to insert a number on a given position
        return boolean
        """

        if num in self.board[pos[0]]:
            return False

        for i_index in range(self.size):
            if num == self.board[i_index][pos[1]]:
                return False

        start_i, start_j = pos[0] // 3, pos[1] // 3
        for i_index in range(start_i*3, start_i*3 + 3):
            for j_index in range(start_j*3, start_j*3 + 3):
                if num == self.board[i_index][j_index]:
                    return False

        return True

    def solve(self):
        """
        Solve sudoku board
        """

        num_pos = self.find_empty()
        if not num_pos:
            return True
        for num in range(1, 10):
            if self.validate(num_pos, num):
                self.board[num_pos[0]][num_pos[1]] = num
                self.steps.append((num, num_pos[0], num_pos[1]))

                if self.solve():
                    return True

        self.board[num_pos[0]][num_pos[1]] = 0
        self.steps.append((0, num_pos[0], num_pos[1]))
        return False

    def get_steps(self):
        """
        Show all steps needed to solve sudoku with backtracking
        return list
        """

        return self.steps

    def run(self):
        """
        Run the Solver
        """

        print(self)
        print("Solving the sudoku...")
        self.solve()
        print("Solving done\n")
        print(self)

test_board = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]


def run_solver():
    new_solver = Solver(test_board)
    new_solver.run()

# runSolver()
