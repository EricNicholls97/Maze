from matrix import Matrix

import random, time, math

# TODO: move scoring metrics to maze factory

# TODO: make matrix private (later so you can test in driver)
class Maze:
    def __init__(self, nrows, ncols):
        self.nrows = nrows
        self.ncols = ncols

        self.matrix = Matrix(nrows, ncols)

    def build_maze(self, p):
        self.matrix.braid(p)
        # self.matrix.remove_all_squares()

        # dends = 1
        # squares = 1
        # while dends > 0 and squares > 0:
        #     self.matrix.braid(p)
        #     squares = self.matrix.remove_all_squares()
        #     dends = self.matrix.num_dends()
        #     print("Squares: ", squares)
        #     print("Dends: ", dends)
        # while self.matrix.remove_all_squares() > 0:
        #     self.matrix.braid(p)

        self.matrix.remove_all_basic_6_chains()

        self.matrix.draw_arr = self.matrix.get_drawable_arr()

    def get_walls(self):
        return self.matrix.get_horz_walls(), self.matrix.get_vert_walls()

    def remove_all_squares(self):
        self.matrix.remove_all_squares()

    def can_I_travel(self, loc_tup, direction_str):
        map = {"right": "R", "left": "L", "up": "U", "down": "D"}
        return self.matrix.can_I_travel(loc_tup[0], loc_tup[1], map[direction_str])

    def get_wall_sparsity_metric(self):
        # 3 x 3
        wall_sparsity = self.matrix.get_wall_sparsity_metric()
        score = self.__score_wall_sparsity__(wall_sparsity)
        return wall_sparsity, score

    def __score_wall_sparsity__(self, wall_sparsity):
        if wall_sparsity <= 0:
            return 10
        if wall_sparsity <= 1:
            return 9
        if wall_sparsity <= 2:
            return 8
        if wall_sparsity <= 3:
            return 7
        if wall_sparsity <= 4:
            return 6
        if wall_sparsity <= 5:
            return 5
        if wall_sparsity <= 6:
            return 4
        if wall_sparsity <= 7:
            return 3
        return 0

    def get_k_metric(self, k):
        v = self.matrix.count_basic_k_metric(k)
        sc = self.__score_6_metric(v)
        return v, sc

    def __score_6_metric(self, score):
        if score <= 25:
            return 10
        if score <= 28:
            return 9
        if score <= 32:
            return 8
        if score <= 36:
            return 7
        if score <= 40:
            return 6
        if score <= 43:
            return 5
        if score <= 46:
            return 4
        if score <= 50:
            return 3
        if score <= 55:
            return 2
        return 1

    def num_horz_walls(self):
        return self.matrix.num_horz_walls()

    def num_vert_walls(self):
        return self.matrix.num_vert_walls()

    def get_all_shortest_loops_metric(self):
        value = self.matrix.count_all_shortest_loops_metric()
        score = self.__score_shortest_loops__(value)
        return value, score

    def __score_shortest_loops__(self, value):
        if value >= 8750:
            return 10
        if value >= 8500:
            return 9
        if value >= 8250:
            return 8
        if value >= 8000:
            return 7
        if value >= 7750:
            return 6
        if value >= 7600:
            return 5
        if value >= 7400:
            return 4
        if value >= 7200:
            return 3
        if value >= 6800:
            return 2
        if value >= 6500:
            return 1
        return 0

    def braid(self, p=1.0):
        self.matrix.braid(p)

