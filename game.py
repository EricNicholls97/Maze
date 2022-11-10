from matrix import Matrix
from maze import Maze
from painter import Painter
from objecto import Objecto
from player import Player

import maze_factory

import datetime, time, random, pygame


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.rows = 30
        self.cols = 30
        # self.game_arr = [[None] * self.cols for _ in range(self.rows)] # store all objects in game obj list

        self.game_object_dict = {}

        self.current_maze = None
        self.num_mazes = 100

        self.num_players = 1
        self.players_list = []

    def create_game(self):
        # creates maze from factory, items, starts looping each player
        print(f"\ncreating mazes ({self.num_mazes})\n")

        m = maze_factory.create_maze(self.num_mazes, self.rows, self.cols)
        self.current_maze = m

        self.__create_chances__(8)

        self.__create_and_start_players__()

    def get_object_list(self):
        print("Dict verion: ", list(self.game_object_dict.values()))
        return list(self.game_object_dict.values())

    def __create_and_start_players__(self):
        for i in range(self.num_players):
            p = Player(self.current_maze, self.rows, self.cols)
            self.players_list.append(p)

        for el in self.players_list:
            el.game_loop()

    def __create_chances__(self, num_chances):
        i = 0
        while i < num_chances:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if (r, c) in self.game_object_dict.keys():
                continue
            spr = Objecto((r, c), 'chance')
            self.game_object_dict[(r, c)] = spr
            i += 1

    def get_all_drawables(self):
        a = []
        for key in self.game_object_dict.keys():
            objecto = self.game_object_dict[key]
            a.append (objecto.get_drawable())


def main():
    g = Game()
    g.create_game()


if __name__ == '__main__':
    main()

# TODO: videos - 2 - spiral from inside and general take (repeat until good takes, put at start)
