from matrix import Matrix
from maze import Maze
from painter import Painter
from player import Player
from item import Item

import maze_factory

import datetime, time, random, pygame


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.rows = 25
        self.cols = 25
        # self.game_arr = [[None] * self.cols for _ in range(self.rows)] # store all objects in game obj list

        self.game_obj_dict = {}

        self.player = Player(self.rows, self.cols)

        self.current_maze = None
        self.num_mazes = 1

    def new_game(self):
        print("\ncreating maze\n")

        m = maze_factory.create_maze(self.num_mazes, self.rows, self.cols)
        self.current_maze = m

        self.__create_game__(m)
        print("Ready to play!")

        self.player.game_loop()

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

    def get_maze_walls(self):
        return self.current_maze.get_vert_walls(), self.current_maze.get_horz_walls()

    def __get_array_of_game_obj_dict__(self, obj_dict):
        return list(obj_dict.values())

def main():
    g = Game()
    g.new_game()

main()