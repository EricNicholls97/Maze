from matrix import Matrix
from maze import Maze
from painter import Painter
from item import Item
from player import Player

import maze_factory

import datetime, time, random, pygame


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.rows = 25
        self.cols = 25
        # self.game_arr = [[None] * self.cols for _ in range(self.rows)] # store all objects in game obj list

        self.painter = Painter(self.rows, self.cols)

        self.game_obj_dict = {}

        self.player1 = Player(self.rows, self.cols)

        self.current_maze = None
        self.num_mazes = 1

    def new_game(self):
        print("\ncreating maze\n")

        m = maze_factory.create_maze(self.num_mazes, self.rows, self.cols)
        self.current_maze = m

        self.__create_game__(m)
        print("Ready to play!")

        pygame.init()
        self.game_loop()

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

    def draw_game(self):
        self.painter.clear()

        # draw maze
        a = self.get_maze_walls()
        self.painter.draw_maze(a[0], a[1])

        # draw game objects (items)
        for obj in self.__get_array_of_game_obj_dict__(self.game_obj_dict):
            obj_drawable = obj.get_drawable()
            self.painter.draw_object(*obj_drawable)

        # draw player
        player_drawable = self.player1.get_drawable()   # r, c, img_link
        self.painter.draw_object(*player_drawable)

    def game_loop(self):
        clock = pygame.time.Clock()
        while True:
            self.get_pygame_input()
            self.painter.clear()
            self.draw_game()
            self.painter.zoom(50, self.player1.get_loc())
            self.painter.update()
            clock.tick(60)

    def get_pygame_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.new_game()
                if event.key == pygame.K_w:
                    self.__check_and_move_player__("up")
                if event.key == pygame.K_a:
                    self.__check_and_move_player__("left")
                if event.key == pygame.K_s:
                    self.__check_and_move_player__("down")
                if event.key == pygame.K_d:
                    self.__check_and_move_player__("right")

        return True

    def __check_and_move_player__(self, direction_str):
        if self.current_maze.can_I_travel(self.player1.get_loc(), direction_str):
            self.__move__(direction_str)

    def __move__(self, dir_str):
        dic = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
        loc_off = dic[dir_str]
        self.player1.move_loc(loc_off[0], loc_off[1])

    def get_maze_walls(self):
        return self.current_maze.get_vert_walls(), self.current_maze.get_horz_walls()

    def __get_array_of_game_obj_dict__(self, obj_dict):
        return list(obj_dict.values())

def main():
    g = Game()
    g.new_game()

main()