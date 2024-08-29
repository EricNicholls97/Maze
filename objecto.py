

class Chests:
    def __init__(self, loc, type):
        self.row = loc[0]
        self.col = loc[1]
        self.type = type
        self.img = None
        if self.type == 'chance':
            self.img = 'Sprites/question_mark.png'


    def __get_img__(self):
        return self.img

    def get_loc(self):
        return self.row, self.col

    def get_drawable(self):
        return self.row, self.col, self.__get_img__()

    def move_loc(self, r, c):
        self.row += r
        self.col += c