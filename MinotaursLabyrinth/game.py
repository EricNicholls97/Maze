import random

from player import Player


class Game:
    def __init__(self, m):
        self.m = m
        self.rows = m.height
        self.cols = m.width
        self.game_arr = [[None] * self.cols for _ in range(self.rows)]

        self.game_obj_list = []

        self.player1 = Player(self.rows - 1, random.randint(0, self.cols - 1))


    def create_game(self):
        num_objs = 10
        for i in range(num_objs):
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)

            if self.game_arr[r][c] is None:
                chance = self.Chance()
                self.game_arr[r][c] = chance

    def get_paintable_list(self):
        a = []
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.game_arr[r][c]
                if cell is None:
                    continue
                str = ""
                if isinstance(cell, self.Chance):
                    str = "?"

                a.append((r, c, str))

        return a

    def get_player_loc(self):
        return self.player1.get_loc()

    class Chance:
        def __init__(self):
            self.seed = random.randint(3, 7)
