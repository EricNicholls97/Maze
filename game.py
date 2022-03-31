from matrix import Matrix
from maze import Maze
from painter import Painter
from player import Player
from item import Item

import maze_factory

import datetime, time, random, pygame


class Game:
    def __init__(self, width):
        self.clock = pygame.time.Clock()

        self.rows = 25
        self.cols = 25
        # self.game_arr = [[None] * self.cols for _ in range(self.rows)] # store all objects in game obj list

        self.game_obj_dict = {}

        # self.player1 = self.Sprite((self.rows - 1, random.randint(0, self.cols - 1)), 'player')
        st_r = self.rows - 1
        st_c = random.randint(0, self.cols - 1)
        self.player = Player((st_r, st_c))

        self.UI_bar_perc = 0.30
        self.UI_bar = self.UI_bar_perc * width
        height = width - self.UI_bar

        self.painter = Painter(width, height, self.UI_bar, self.rows, self.cols)

        self.current_maze = None
        self.num_mazes = 1

    def new_game(self):
        print("\ncreating maze\n")

        m = maze_factory.create_maze(self.num_mazes, self.rows, self.cols)
        self.current_maze = m

        self.__create_game__(m)
        print("Ready to play!")
        self.painter.draw_maze(self.current_maze.get_vert_walls(), self.current_maze.get_horz_walls())

        self.player.game_loop()

    def draw_maze(self):
        # self.painter.clear()

        # draw w/ Painter
        self.painter.draw_foundation()

        # draw objects (TODO)
        game_obj_list = self.__get_array_of_game_obj_dict__(self.game_obj_dict)


    def __create_game__(self, m):
        # add chances
        # store in dict game_obj_dict
        num_chances = 8
        i = 0
        while i < num_chances:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if (r, c) in self.game_obj_dict.keys():
                continue
            spr = Item((r, c), 'chance')
            self.game_obj_dict[(r, c)] = spr
            i += 1

    def __get_array_of_game_obj_dict__(self, obj_dict):
        return list(obj_dict.values())


def main():
    g = Game(1000)
    g.new_game()

main()