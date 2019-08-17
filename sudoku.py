import pygame
import time
from solver import Solver


class Sudoku:

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    SIZE = 56

    def __init__(self, board, win_side):
        pygame.init()
        self.board = board
        self.win_side = win_side
        self.size = (win_side, win_side)
        self.offset = self.win_side/(len(self.board)-1)
        self.font = pygame.font.Font(pygame.font.get_default_font(), self.SIZE)
        self.run = True

    def on_init(self):
        """
        Initialize before the main loop
        """

        self.win = pygame.display.set_mode(self.size)
        self.draw_grid()
        self.draw_numbers()
        pygame.display.set_caption("Sudoku")

    def draw_grid(self):
        """
        Draw grid
        """
        self.win.fill(self.WHITE)

        for i in range(1, len(self.board)):
            pygame.draw.line(self.win, self.BLACK, (self.offset*i, 0), (self.offset*i, self.win_side), 2)
            pygame.draw.line(self.win, self.BLACK, (0, self.offset*i), (self.win_side, self.offset*i), 2)

    def draw_number(self, num, x, y):
        """
        Draw number on a given position
        """

        num = str(num)
        text = self.font.render(num, True, self.BLACK)
        pygame.draw.rect(self.win, self.WHITE, pygame.Rect(x-text.get_width()/2, y-text.get_height()/2, 54, 54))
        if not num == '0':
            self.win.blit(text, (x-text.get_width()/2, y-text.get_height()/2))

    def draw_numbers(self):
        """
        Draw all given numbers based on the starting board
        """

        for row_idx, row in enumerate(self.board):
            for col_idx, number in enumerate(row):
                if number == 0:
                    continue

                x, y = self.get_coordinates(row_idx, col_idx)
                self.draw_number(number, x, y)

    def get_coordinates(self, row, col):
        """
        Get x and y coordinates for drawing number
        return variables
        """

        x = self.offset * col + self.offset / 2
        y = self.offset * row + self.offset / 2
        return x, y

    def solve_sudoku(self):
        """
        Solve the sudoku using Solver and show the steps
        """

        solver = Solver(self.board)
        solver.solve()
        for i in solver.get_steps():
            x, y = self.get_coordinates(i[1], i[2])
            self.draw_number(i[0], x, y)
            pygame.display.update()
            time.sleep(0.2)

    def on_event(self, event):
        """
        Check for events
        """

        if event.type == pygame.QUIT:
            self.run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.solve_sudoku()

    def on_loop(self):
        """
        Compute changes in the game
        """

        # TODO: Make the game playable

    def on_render(self):
        """
        Render all graphics
        """

        pygame.display.update()

    def main(self):
        """
        Creates the main loop
        """
        self.on_init()

        while self.run:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()

        pygame.quit()
        quit()

test_board = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]

if __name__ == "__main__":
    sudokuGame = Sudoku(test_board, 800)
    sudokuGame.main()
