import pygame, time

cyan = (0, 200, 255)
black = (0, 0, 0)


class Painter:
    global cyan, black

    def __init__(self, nrows, ncols):

        self.nrows = nrows

        full_width = 1800
        UI_perc = 0.3

        self.UI_bar_len = UI_perc * full_width

        self.game_width = full_width - self.UI_bar_len
        self.game_height = self.game_width

        pygame.init()

        pygame.display.set_caption('Minotaurs Labyrinth')
        self.border = 500
        self.screen = pygame.display.set_mode((self.game_width, self.game_height))

        self.cell_width = self.game_width / ncols
        self.cell_height = self.game_height / nrows

        factor = 2/3
        sz_w = self.cell_width * factor
        sz_h = self.cell_height * factor
        self.object_sizes = (sz_w, sz_h)

        # self.metrics_written = 1

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

        self.metrics_written += 1

    def draw_maze(self, horz, vert):
        w = self.cell_width
        h = self.cell_height

        for i in range(len(vert)):
            for j in range(len(vert[0])):
                i2 = i + 1
                j2 = j + 1
                if vert[i][j] == 1:
                    # print((j2*w, i*h), (j2*w, i2*h))
                    pygame.draw.line(self.screen, cyan, (j2*w, i*h), (j2*w, i2*h))

        for i in range(len(horz)):
            for j in range(len(horz[0])):
                i2 = i + 1
                j2 = j + 1
                if horz[i][j] == 1:
                    pygame.draw.line(self.screen, cyan, (j*w, i2*h), (j2*w, i2*h))

        # left, bottom, top line (right line is UI line)

        # pygame.draw.line(self.screen, cyan, (1, 0), (1, self.game_height))   # left
        # pygame.draw.line(self.screen, cyan, (0, self.game_height-1), (self.game_width, self.game_height-1))   # bottom
        # pygame.draw.line(self.screen, cyan, (0, 1), (self.game_width, 1))  # top

        # UI line / right line
        # pygame.draw.line(self.screen, cyan, (self.game_width-1, 0), (self.game_width-1, self.game_height))

    def draw_object(self, r, c, image_link):
        my_img = pygame.image.load(image_link)
        x = (c + 1/8) * self.cell_width
        y = (r + 1/8) * self.cell_height

        my_img = pygame.transform.scale(my_img, self.object_sizes)

        self.screen.blit(my_img, (x, y))

    def clear(self):
        self.screen.fill((0, 0, 0))

    def zoom_func(self, zoom, x, y):
        zoom_size = (self.game_width / zoom, self.game_height / zoom)
        zoom_area = pygame.Rect(0, 0, *zoom_size)
        zoom_area.center = (x - zoom_size[0]/2, y - zoom_size[1]/2)     # subtract half of width/ height to get center
        zoom_surf = pygame.Surface(zoom_area.size)
        zoom_surf.blit(self.screen, (0, 0), zoom_area)
        zoom_surf = pygame.transform.smoothscale(zoom_surf, (self.game_width, self.game_height))
        self.screen.blit(zoom_surf, (0, 0))

    def zoom(self, num_rows, loc):
        inv_ratio = self.nrows / num_rows   # num_rows was length    # inverse of ratio
        zoom = inv_ratio
        adjust = self.game_height / 2
        x = loc[1] * self.cell_width
        y = loc[0] * self.cell_height
        self.zoom_func(zoom, x + adjust/zoom, y + adjust/zoom)

    def update(self):
        pygame.display.flip()

    class Sprite (pygame.sprite.Sprite):
        def __init__(self, x, y, wid, hei, sprite_img):
            super().__init__()
            self.rect = pygame.Rect(x, y, wid, hei)

            image = pygame.image.load(sprite_img)
            self.image = pygame.transform.scale(image.convert_alpha(), (wid*2/3, hei*2/3))
