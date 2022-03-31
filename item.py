

class Item:
    def __init__(self, loc, type):
        self.row = loc[0]
        self.col = loc[1]
        self.type = type

    def get_img(self):
        if self.type == 'chance':
            return 'Sprites/question_mark.png'

    def get_loc(self):
        return self.row, self.col

    def move_loc(self, r, c):
        self.row += r
        self.col += c