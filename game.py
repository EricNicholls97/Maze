from matrix import Matrix
from maze import Maze
from painter import Painter

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
        self.player1 = self.Sprite((0, 0), 'player')

        self.UI_bar_perc = 0.30
        self.UI_bar = self.UI_bar_perc * width
        height = width - self.UI_bar

        w = width / (self.cols + 1)
        h = height / self.rows
        self.painter = Painter(width, height, self.UI_bar, self.rows, self.cols)

        self.current_maze = None
        self.num_mazes = 1

    def new_game(self):
        print("\ncreating maze\n")

        m = maze_factory.create_maze(self.num_mazes, self.rows, self.cols)
        self.current_maze = m

        self.__create_game__(m)
        print("Ready to play!")
        self.draw_game()

        self.game_loop()

    def draw_game(self):
        # self.painter.clear()

        # draw w/ Painter
        self.painter.draw_foundation()
        self.painter.draw_maze_lines(self.current_maze.get_vert_walls(), self.current_maze.get_horz_walls())

        # draw objects (TODO)
        game_obj_list = self.__get_array_of_game_obj_dict__(self.game_obj_dict)

        # draw player
        loc = self.player1.get_loc()
        img = self.player1.get_img()
        self.painter.draw_object(loc[0], loc[1], img)

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
            spr = self.Sprite((r, c), 'chance')
            self.game_obj_dict[(r, c)] = spr
            i += 1

    def __get_array_of_game_obj_dict__(self, obj_dict):
        return list(obj_dict.values())

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

    class Sprite:
        def __init__(self, loc, type):
            self.row = loc[0]
            self.col = loc[1]
            self.type = type

        def get_img(self):
            if self.type == 'player':
                return 'Sprites/purple_pink.png'
            if self.type == 'chance':
                return 'Sprites/question_mark.png'

        def get_loc(self):
            return self.row, self.col

        def move_loc(self, r, c):
            self.row += r
            self.col += c

def main():
    g = Game(1000)
    g.new_game()

main()