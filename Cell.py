import pygame


class Cell:
    def __init__(self, activate=False, dct_colors=None):
        self.dct_colors_deafult = {True: pygame.Color(255, 255, 255), False: pygame.Color(0, 0, 0)}
        if dct_colors is None:
            dct_colors = self.dct_colors_deafult
        self.color = dct_colors[activate]
        self.activate = activate

    def change_activate(self, activate=False, dct_colors=None):
        if dct_colors is None:
            dct_colors = self.dct_colors_deafult
        self.color = dct_colors[activate]
        self.activate = activate
