import pygame, random, math


from painter import Painter
from visibility import Visibility

class Player:
    def __init__(self, maze, nrows, ncols):

        self.maze = maze
        self.maze_lines = maze.get_walls()

        self.nrows = nrows
        self.ncols = ncols

        self.img = 'Sprites/purple_pink.png'
        self.row = nrows - 1
        self.col = random.randint(0, ncols - 1)

        self.visibility = Visibility(nrows, ncols)
        self.__set_visibility__(self.row, self.col)

        self.painter = Painter(nrows, ncols)


    def get_img(self):
        return self.img

    def get_loc(self):
        return self.row, self.col

    def get_drawable(self):
        return self.row, self.col, self.img

    def move_loc(self, r, c):
        self.row += r
        self.col += c
        self.__set_visibility__(self.row, self.col)

    def __set_visibility__(self, row, col):
        a = []
        for i in range(-1, 2, 2):
            r = row + i
            if r in range(0, self.nrows):
                a.append((r, col))

        for i in range(-1, 2):
            c = col + i
            if c in range(0, self.ncols):
                a.append((row, c))

        self.visibility.add_visibility(a)

    def draw_game(self):
        # calculate r1, r2, c1, c2
        # create a new maze lines array using r1, r2, c1, c2
        # create list of all items as tuples (r, c, img_link)
        # call draw_game (sub_rows, sub_cols, lines, item_list)

        # r1, r2, c1, c2 = self.visibility.get_edges()
        # # TODO: get maze lines subarray for vertical and horizonal
        # # upd_maze_lines = ___
        # subrows = r2 - r1
        # subcols = c2 - c1
        #
        # # TODO (later): (HARD) calculate which maze lines to draw using visibility array
        # # for now, just draw all the lines in the right place
        #
        # item_list = game.get_object_list()
        #
        # painter.draw_game(subrows, subcols, upd_maze_lines, item_list)
        self.painter.clear()

        upd_lines = self.visibility.filter_walls(*self.maze_lines)

        self.painter.draw_maze(*upd_lines)
        self.painter.draw_object(self.row, self.col, self.img)

        loc, diffs = self.visibility.get_location_specs()
        sq = max(diffs)
        self.painter.zoom(sq + 2, loc)

        self.painter.update()

    def game_loop(self):
        clock = pygame.time.Clock()
        while True:
            self.get_pygame_input()
            self.draw_game()
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
        if self.maze.can_I_travel(self.get_loc(), direction_str):
            self.__move__(direction_str)

    def __move__(self, dir_str):
        dic = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
        loc_off = dic[dir_str]
        self.move_loc(loc_off[0], loc_off[1])