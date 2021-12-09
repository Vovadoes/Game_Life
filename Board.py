import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [["black"] * width for _ in range(height)]
        self.dct = {}
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def paint_cell(self, scr, thickness=2, color=None):
        for j in range(self.height):
            for i in range(self.width):
                if color is None:
                    color_n = self.board[j][i]
                else:
                    color_n = color
                pygame.draw.rect(
                    scr,
                    color_n,
                    [
                        self.left + i * self.cell_size,
                        self.top + j * self.cell_size,
                        self.cell_size,
                        self.cell_size
                    ],
                    thickness)

    def render(self, scr):
        self.paint_cell(scr, 0)
        self.paint_cell(scr, 2, pygame.Color(255, 255, 255))

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        if 0 <= x < self.width and 0 <= y < self.height:
            return x, y
        return None

    def on_click(self, cell_coords):
        if cell_coords:
            x, y = cell_coords
            if self.board[y][x] == "black":
                self.board[y][x] = "red"
            elif self.board[y][x] == "red":
                self.board[y][x] = "blue"
            elif self.board[y][x] == "blue":
                self.board[y][x] = "black"

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
