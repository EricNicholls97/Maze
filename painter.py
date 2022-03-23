import pygame, time

cyan = (0, 200, 255)
black = (0, 0, 0)


class Painter:
    global cyan, black

    def __init__(self, width, height, UI_width, nrows, ncols):
        self.zoom = 2

        self.metrics_written = 1

        self.width = width
        self.height = height

        self.UI_width = UI_width
        self.game_width = width - UI_width

        pygame.init()

        self.border = 20
        self.screen = pygame.display.set_mode((width, height))
        # scroll = [0, 0]
        # scroll[0] = 300 - int(self.game_width / (self.zoom * 2)) + 2
        # scroll[1] = 300 - int(self.height / (self.zoom * 2)) + 5
        # self.display.blit(pygame.image.load("Sprites/green_red.png"), (300 - scroll[0], 300 - scroll[1]))

        # self.screen.set_caption('Minotaurs Labyrinth')

        self.cell_width = self.game_width / ncols
        self.cell_height = height / nrows

    def write_metric(self, name, metric_value, metric_score):
        # UI bar text
        dist_between_vert = 60
        len_mult = 3

        text = str(metric_score) + "  |   " + name + "       " + str(metric_value)
        x = self.game_width + self.UI_width//2 - len(text)*len_mult
        y = self.metrics_written * dist_between_vert

        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 25)
        textsurface = myfont.render(text, False, (255, 255, 255))
        self.screen.blit(textsurface, (x, y))

        self.update()

        self.metrics_written += 1

    def draw_foundation(self):
        # clear screen
        self.screen.fill((0, 0, 0))

        # left, bottom, top line (right line is UI line)
        pygame.draw.line(self.screen, cyan, (1, 0), (1, self.height))   # left
        pygame.draw.line(self.screen, cyan, (0, self.height-1), (self.game_width, self.height-1))   # bottom
        pygame.draw.line(self.screen, cyan, (0, 1), (self.game_width, 1))  # top

        # UI line / right line
        pygame.draw.line(self.screen, cyan, (self.game_width-1, 0), (self.game_width-1, self.height))

        self.update()

    def draw_maze_lines(self, vert, horz):
        w = self.cell_width
        h = self.cell_height

        for i in range(len(vert)):
            for j in range(len(vert[0])):
                i2 = i + 1
                j2 = j + 1
                if vert[i][j] == 1:
                    pygame.draw.line(self.screen, cyan, (j2*w, i*h), (j2*w, i2*h))

        for i in range(len(horz)):
            for j in range(len(horz[0])):
                i2 = i + 1
                j2 = j + 1
                if horz[i][j] == 1:
                    pygame.draw.line(self.screen, cyan, (j*w, i2*h), (j2*w, i2*h))

        # self.zoom_func(2, 0, 0)
        # ? : chance
        self.update()

    def draw_object(self, r, c, image_link):
        my_img = pygame.image.load(image_link)
        x = (c + 1/5) * self.cell_width
        y = (r + 1/5) * self.cell_height

        self.screen.blit(my_img, (x, y))
        self.update()

    def clear(self):
        self.screen.fill((0, 0, 0))

    # def add_group_chance(self, obj_list):
    #     if self.group_chance is not None:
    #         self.group_chance.clear(self.screen, pygame.Surface((self.width, self.height)))
    #     self.group_chance = pygame.sprite.Group()
    #     w = self.cell_width
    #     h = self.cell_height
    #
    #     for el in obj_list:
    #         el_loc = el.get_loc()
    #         x = el_loc[1] * w + (w * 1/5)
    #         y = el_loc[0] * h + (h * 1/5)
    #         el_img = el.get_img()
    #         spr = self.Sprite(x, y, w, h, el_img)
    #         self.group_chance.add(spr)
    #
    # def add_group_player(self, player):
    #     if self.group_player is not None:
    #         self.group_player.clear(self.screen, pygame.Surface((self.width, self.height)))     # clear group w/ surface
    #     self.group_player = pygame.sprite.Group()
    #     w = self.cell_width
    #     h = self.cell_height
    #
    #     ploc = player.get_loc()
    #     x = ploc[1] * w + (w * 1 / 5)
    #     y = ploc[0] * h + (h * 1 / 5)
    #     p_img = player.get_img()
    #     spr = self.Sprite(x, y, w, h, p_img)
    #
    # def draw_group_chance(self):
    #     self.group_chance.draw(self.screen)
    #     self.zoom_func_2(2, 0, 0)
    #     self.update()
    #
    # def draw_group_player(self):
    #     self.group_player.draw(self.screen)
    #     self.zoom_func_2(2, 0, 0)
    #     self.update()

    def zoom_func(self, zoom, x, y):
        zoom_size = (self.game_width / zoom, self.height / zoom)
        zoom_area = pygame.Rect(0, 0, *zoom_size)
        zoom_area.center = (x, y)
        zoom_surf = pygame.Surface(zoom_area.size)
        zoom_surf.blit(self.screen, (0, 0), zoom_area)
        zoom_surf = pygame.transform.smoothscale(zoom_surf, (self.game_width, self.height))
        self.screen.blit(zoom_surf, (0, 0))

    def update(self):
        self.zoom_func(1, -100, -100)
        pygame.display.update()

    class Sprite (pygame.sprite.Sprite):
        def __init__(self, x, y, wid, hei, sprite_img):
            super().__init__()
            self.rect = pygame.Rect(x, y, wid, hei)

            image = pygame.image.load(sprite_img)
            self.image = pygame.transform.scale(image.convert_alpha(), (wid*2/3, hei*2/3))
