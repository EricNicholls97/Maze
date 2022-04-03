

class Visibility:
    def __init__(self, rows, cols):
        self.arr = [[False for _ in range(rows)] for _ in range(cols)]

        # test
        for i in range(25):
            self.arr[24][i] = True

        self.write_arr()

        self.min_row = -1
        self.max_row = -1
        self.min_col = -1
        self.max_col = -1

    def write_arr(self):
        for row in self.arr:
            for el in row:
                print('X' if el is False else 'O', end=" ")
            print()

    def add_visibility(self, cell_list):
        pass

    def get_minmax_row(self):
        return self.min_row, self.max_row

    def get_min_max_col(self):
        return self.min_col, self.max_col