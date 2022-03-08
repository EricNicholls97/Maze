

class Player:
    def __init__(self, st_row, st_col):
        self.row = st_row
        self.col = st_col

    def get_loc(self):
        return self.row, self.col