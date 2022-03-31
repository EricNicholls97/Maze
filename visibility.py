

class Visibility:
    def __init__(self):
        self.arr = [[False for _ in range(rows)] for _ in range(cols)]
        # test
        self.arr[0][1] = True
        print(self.arr)

        self.min_row = -1
        self.max_row = -1
        self.min_col = -1
        self.max_col = -1

    def add_visibility(self, cell_list):
        pass

    def get_minmax_row(self):
        return self.min_row, self.max_row

    def get_min_max_col(self):
        return self.min_col, self.max_col