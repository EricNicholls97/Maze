import pygame, random

from painter import Painter
import game

class Player:
    def __init__(self, nrows, ncols):
        self.painter = Painter(nrows, ncols)

        self.img = 'Sprites/purple_pink.png'
        self.row = nrows - 1
        self.col = random.randint(0, ncols - 1)

        self.game = game.Game()

    def get_img(self):
        return self.img

    def get_loc(self):
        return self.row, self.col

    def move_loc(self, r, c):
        self.row += r
        self.col += c

    def draw_game(self):
        # draw Game
        all_objs_list = self.game.__get_array_of_game_obj_dict__(self, obj_dict)
        # draw player
        loc = self.get_loc()
        img = self.get_img()
        self.painter.draw_object(loc[0], loc[1], img)

        a = self.game.get_maze()
        self.painter.draw_maze(a)

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
        self.move_loc(loc_off[0], loc_off[1])