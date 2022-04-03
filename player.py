import pygame, random

from painter import Painter
from visibility import Visibility

class Player:
    def __init__(self, nrows, ncols):
        self.img = 'Sprites/purple_pink.png'
        self.row = nrows - 1
        self.col = random.randint(0, ncols - 1)

        self.visibility = Visibility(nrows, ncols)

    def get_img(self):
        return self.img

    def get_loc(self):
        return self.row, self.col

    def get_drawable(self):
        return self.row, self.col, self.img

    def move_loc(self, r, c):
        self.row += r
        self.col += c
