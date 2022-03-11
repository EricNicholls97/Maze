from matrix import Matrix
from maze import Maze
from painter import Painter

import maze_factory

import datetime, time, random, pygame

class Game:
    def __init__(self):
        self.rows = 25
        self.cols = 25
        # self.game_arr = [[None] * self.cols for _ in range(self.rows)] # store all objects in game obj list

        self.game_obj_dict = {}

        self.player1 = self.Player(self.rows - 1, random.randint(0, self.cols - 1))
        self.player_sprite_direc = pygame.image.load('Sprites/purple_pink.png')

        self.painter = Painter(1800, 1100, 800)

        self.current_maze = None
        self.num_mazes = 1


    def new_game(self):
        print("\ncreating maze\n")

        m = maze_factory.create_maze(self.num_mazes, self.rows, self.cols)

        self.current_maze = m
        self.__create_game__(m)

        print("Maze + Game Ready")
        self.draw_game()

        self.game_loop()

    def draw_game(self):
        # draw w/ Painter
        self.painter.draw_foundation()
        self.painter.draw_maze_lines(self.current_maze.get_vert_walls(), self.current_maze.get_horz_walls())

        # painter draw_game
        self.painter.draw_game(self.player1.get_loc(), self.__get_array_of_game_obj_dict__(self.game_obj_dict), self.player_sprite_direc)

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
            chance = self.Chance()
            self.game_obj_dict[(r, c)] = chance
            i += 1

    def __get_array_of_game_obj_dict__(self, obj_dict):
        a = []      # stores (row, col, symbol)
        for (r, c) in obj_dict.keys():
            a.append((r, c, obj_dict[(r, c)].get_symbol()))
        return a

    # how do you continuously update paint
    def game_loop(self):
        FPS = 60
        cur_time = time.time()  # use to calculate fps

        keep_running = True
        while keep_running:

            if not self.get_pygame_input():  # gets pygame input events
                keep_running = False

            # self.draw_game()

            # last_time = cur_time
            # cur_time = time.time()
            # self.wait(cur_time, last_time)

        pass
        # get user input. move player,

    def wait(self, current_time, last_frame_time):
        time.sleep(1)

        # FPS = 60
        #
        # sleep_time = 1. / FPS - (current_time - last_frame_time)
        # if sleep_time > 0:
        #     time.sleep(sleep_time)

    def __move_player__(self, direction_str):
        self.player1.move(direction_str)
        self.draw_game()

    def get_pygame_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.K_RETURN:
                    pass    # TODO:
                if event.key == pygame.K_w:
                    self.__move_player__("up")
                if event.key == pygame.K_a:
                    self.__move_player__("left")
                if event.key == pygame.K_s:
                    self.__move_player__("down")
                if event.key == pygame.K_d:
                    self.__move_player__("right")

                if event.key == pygame.K_RIGHT:
                    print("Right")

        return True

    class Chance:
        def __init__(self):
            self.seed = random.randint(3, 7)

        def get_symbol(self):
            return "?"

    class Player:
        def __init__(self, st_row, st_col):
            self.row = st_row
            self.col = st_col

        def get_loc(self):
            return self.row, self.col

        # direction = 0: left   1: right   2: up   3: down
        def move(self, direction_str):
            if direction_str == "left":
                self.col -= 1
            if direction_str == "right":
                self.col += 1
            if direction_str == "up":
                self.row -= 1
            if direction_str == "down":
                self.row += 1