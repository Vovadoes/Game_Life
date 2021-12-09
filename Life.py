import pygame
from Cell import Cell
from copy import deepcopy
from Board import Board


class Life(Board):
    # создание поля
    def __init__(self, width, height):
        super().__init__(width, height)
        self.board = [[Cell() for _ in range(width)] for _ in range(height)]

    def paint_cell(self, scr, thickness=2, indent=1, color=None):
        if thickness != 0:
            indent = 0
        for j in range(self.height):
            for i in range(self.width):
                if color is None:
                    color_n = self.board[j][i].color
                else:
                    color_n = color
                pygame.draw.rect(
                    scr,
                    color_n,
                    [
                        self.left + i * self.cell_size + indent,
                        self.top + j * self.cell_size + indent,
                        self.cell_size - indent,
                        self.cell_size - indent
                    ],
                    thickness)

    def adjacent_cells(self, y, x, key_area=None):
        if key_area is None:
            key_area = {self.board[y][x].activate}
        n = 0
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if self.board[i % self.height][j % self.width].activate in key_area:
                    n += 1
        return n

    def next_move(self):
        board = deepcopy(self.board)
        for i in range(self.height):  # y
            for j in range(self.width):  # x
                if board[i][j].activate:
                    if 2 <= self.adjacent_cells(i, j, {True}) - 1 <= 3:
                        pass
                    else:
                        board[i][j].change_activate(False)
                else:
                    if self.adjacent_cells(i, j, {True}) == 3:
                        board[i][j].change_activate(True)
        self.board = board

    def render(self, scr):
        self.paint_cell(scr, 2, color=pygame.Color(255, 255, 255))
        self.paint_cell(scr, 0, 1)

    def on_click(self, cell_coords):
        if cell_coords:
            x, y = cell_coords
            self.board[y][x].change_activate(not self.board[y][x].activate)
