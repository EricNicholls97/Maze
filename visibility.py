import math
import copy

class Visibility:
    def __init__(self, rows, cols):
        self.arr = [[False for _ in range(rows)] for _ in range(cols)]

        self.nrows = rows
        self.ncols = cols

        self.min_row = math.inf
        self.max_row = -math.inf
        self.min_col = math.inf
        self.max_col = -math.inf

    def write_arr(self):
        for row in self.arr:
            for el in row:
                print('X' if el is False else 'O', end=" ")
            print()

    def add_visibility(self, cell_list):
        for cell in cell_list:
            r = cell[0]
            c = cell[1]
            self.arr[r][c] = True
            if r < self.min_row:
                self.min_row = r
            if r > self.max_row:
                self.max_row = r
            if c < self.min_col:
                self.min_col = c
            if c > self.max_col:
                self.max_col = c

            # trying to make edges more natural by increasin
            if self.min_row==0:
                self.min_row = -1
            if self.min_col==0:
                self.min_col = -1
            if self.max_row == self.nrows - 1:
                self.max_row = self.nrows
            if self.max_col == self.ncols - 1:
                self.max_col = self.ncols

        self.__get_my_vert__()  # delete
        print()
        print()

    def get_location_specs(self):
        # returns halfway point for row, col, then row diff and col diff
        halfway = ((self.min_row + self.max_row) / 2, (self.min_col + self.max_col) / 2)        # (rows, cols)
        diff = (self.max_row - self.min_row, self.max_col - self.min_col)                       # (rows, cols)
        return halfway, diff

    def get_square_size(self):
        # finds the bigger difference (row max-min vs. col max-min)
        if self.max_row - self.min_row > self.max_col - self.min_col:
            return self.max_row - self.min_row
        else:
            return self.max_col - self.min_col

    def get_min_max_row(self):
        return self.min_row, self.max_row

    def get_min_max_col(self):
        return self.min_col, self.max_col

    def filter_walls(self, horz, vert):
        my_vert = self.__get_my_vert__()
        my_horz = self.__get_my_horz__()
        combined_vert = self.__combine__(vert, my_vert)
        combined_horz = self.__combine__(horz, my_horz)
        return combined_horz, combined_vert

    def __combine__(self, arr1, arr2):
        a = copy.deepcopy(arr1)
        for r in range(len(arr1)):
            for c in range(len(arr1[0])):
                if arr1[r][c] == arr2[r][c] == 1:
                    a[r][c] = 1
                else:
                    a[r][c] = 0
        return a

    def __get_my_vert__(self):
        a = [[0 for _ in range(self.ncols-1)] for _ in range(self.nrows)]

        for r in range(0, self.nrows):
            for c in range(0, self.ncols-1):
                if self.arr[r][c] or self.arr[r][c+1]:
                    a[r][c] = 1
        return a

    def __get_my_horz__(self):
        a = [[0 for _ in range(self.ncols)] for _ in range(self.nrows-1)]

        for r in range(0, self.nrows-1):
            for c in range(0, self.ncols):
                if self.arr[r][c] or self.arr[r+1][c]:
                    a[r][c] = 1
        return a

