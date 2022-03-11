import random
from path_manager import PathManager

#TODO -> path_manager

# default converts from cell coordinates to matrix coordinates
def __convert_coor__(r, c, reverse=False):
    if reverse:
        return r//2, c//2
    return 2*r, 2*c

# everything in matrix coordinates
def __get_neighbors_array__():
    return [[-1, 0], [0, 1], [0, -1], [1, 0]]

# -1: node   0: Empty   1: Wall
# n = num_rows, m = num_cols
# cell coordinates:       r, c
# matrix coordinates:     r1, c1

# the matrix has extra indices to store both the row and column of every 'cell' and every wall.
# matrix coordinates vs cell coordinates
class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.n = 2 * n - 1
        self.m = 2 * m - 1
        self.__arr__ = self.__init_empty_arr__(n, m)
        self.generate_random_maze()

    def __str__(self):
        s = ''
        for row in self.__arr__:
            s += str(row) + '\n'
        return s

    def generate_random_maze(self):
        # gather all Empty passages (places a wall could be but isn't)
        # randomly choose a passage and add a tentative wall
        # check flood method. If True, confirm wall. Otherwise, revert tentative wall back to passage
        # repeat until __?__
        passages = self.__get_all_passages__()   # stored in list of x, y coordinates [[r1, c1], [r2, c2], ...]
        while len(passages) > 0:
            r, c = passages.pop(random.randint(0, len(passages)-1))
            self.__arr__[r][c] = 1      # set passage to Wall
            if self.__flood__() is False:
                self.__arr__[r][c] = 0      # revert passage back to Empty

    # public methods
    # remove a percentage of dead ends
    def braid(self, p=1.0):
        # gather all dead ends. remove one wall of a percentage of them (p)
        dead_ends = self.__get_all_dead_ends__()
        n = len(dead_ends)
        num_to_process = int(len(dead_ends) * p)
        for i in range(num_to_process):
            dead_end = dead_ends.pop(random.randint(0, len(dead_ends) - 1))
            r1, c1 = __convert_coor__(dead_end[0], dead_end[1])
            self.__remove_random_wall__(r1, c1)
            dead_ends = self.__get_all_dead_ends__()
            if len(dead_ends) == 0:
                break


    # TODO: print all chains
    def remove_all_basic_6_chains(self):
        six_rows, six_cols = self.__find_all_basic_6_chains__()

        for el in six_rows:
            r = el[0]
            c = el[1]

            r1, c1 = __convert_coor__(r, c)
            choice_1 = [(r1+1, c1), (r1+3, c1)]
            choice_2 = [(r1+1, c1+4), (r1+3, c1+4)]

            rn = random.randint(0, 1)
            walL_loc_1 = choice_1[rn]
            walL_loc_2 = choice_2[1-rn]

            self.__arr__[walL_loc_1[0]][walL_loc_1[1]] = 1
            self.__arr__[walL_loc_2[0]][walL_loc_2[1]] = 1

        for el in six_cols:
            r = el[0]
            c = el[1]

            r1, c1 = __convert_coor__(r, c)
            choice_1 = [(r1, c1+1), (r1, c1+3)]
            choice_2 = [(r1+4, c1+1), (r1+4, c1+3)]

            walL_loc_1 = random.choice(choice_1)
            walL_loc_2 = random.choice(choice_2)

            self.__arr__[walL_loc_1[0]][walL_loc_1[1]] = 1
            self.__arr__[walL_loc_2[0]][walL_loc_2[1]] = 1

    def __find_all_basic_6_chains__(self):
        rows_six = []
        cols_six = []
        for r in range(self.rows):
            conseq = 0
            for c in range(self.cols):
                b1, b2 = self.__is_basic_six_metric__(r, c, 6)  # returns horizontal, vertical from top left
                if b2:
                    conseq += 1\

                else:
                    conseq = 0
                # following setup catches all conseq = 2 ( so remove function deals with them as pairs)
                if conseq >= 2:
                    rows_six.append((r, c-1, conseq))
                    conseq = 0

        for c in range(self.cols):
            conseq = 0
            for r in range(self.rows):
                b1, b2 = self.__is_basic_six_metric__(r, c, 6)  # returns horizontal, vertical from top left
                if b1:
                    conseq += 1
                if conseq >= 2:
                    cols_six.append((r - 1, c, conseq))
                    conseq = 0

        return rows_six, cols_six


    # convert coordinates. check surrounding segments and return neighbors
    def get_neighbors(self, r, c, open=True):
        open_bool = 1 if open else 0
        r1, c1 = __convert_coor__(r, c)
        a = []
        neighbors = __get_neighbors_array__()
        for neighbor in neighbors:
            new_r = r1 + neighbor[0]
            new_c = c1 + neighbor[1]
            if new_r < 0 or new_r >= self.n or new_c < 0 or new_c >= self.m:
                continue
            if self.__arr__[new_r][new_c] != open_bool:
                a.append([r + neighbor[0], c + neighbor[1]])
        return a

    def get_vert_walls(self):
        vert = []
        # vertical
        for r in range(0, self.n, 2):
            a = []
            for c in range(1, self.m, 2):
                a.append(self.__arr__[r][c])
            vert.append(a)
        return vert

    def get_horz_walls(self):
        hori = []
        # horizontal
        for r in range(1, self.n, 2):
            a = []
            for c in range(0, self.m, 2):
                a.append(self.__arr__[r][c])
            hori.append(a)
        return hori

    def can_I_travel(self, r, c, dir_str):
        m = {'R': 0, 'L': 1, 'U': 2, "D": 3}
        dir = m[dir_str]
        r1, c1 = __convert_coor__(r, c)
        dir_arr = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        new_r = r1 + dir_arr[dir][0]
        new_c = c1 + dir_arr[dir][1]
        if not (0 <= new_r < self.n and 0 <= new_c < self.m):
            return False
        return not self.__arr__[new_r][new_c]

    # returns the count of squares
    # count_squares method if remove=False
    def remove_all_squares(self, remove=True):
        num_squares = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.__is_square__(r, c):
                    num_squares += 1
                    if remove:
                        r1, c1 = __convert_coor__(r, c)
                        passages = [(r1-2, c1-1), (r1-1, c1), (r1, c1-1), (r1-1, c1-2)]   # top, right, down, left (square)
                        rn = random.randint(0, 3)
                        self.__arr__[passages[rn][0]][passages[rn][1]] = 1
        return num_squares

    def count_basic_k_metric(self, k=6):
        count = 0
        a = []

        for r in range(self.rows):
            for c in range(self.cols):
                b1, b2 = self.__is_basic_six_metric__(r, c, k)  # returns horizontal, vertical from top left
                if b1:
                    a.append(__convert_coor__(r, c, True))
                    count += 1
                if b2:
                    a.append(__convert_coor__(r, c, True))
                    count += 1
        return count

    def get_wall_sparsity_metric(self):
        # measure first 3 x 3 region (5 x 5 in matrix coordinates)
        num_under_two = 0
        for c1 in range(0, self.m - 4, 2):
            count = 0
            for i in range(5):
                for j in range(5):
                    if self.__arr__[i][c1 + j] == 1:
                        count += 1

            if count < 2:
                num_under_two += 1

            for r1 in range(0, self.n - 5, 2):
                for i in range(5):
                    # remove top row
                    if self.__arr__[r1][c1 + i] == 1:
                        count -= 1
                    # remove second row
                    if self.__arr__[r1 + 1][c1 + i] == 1:
                        count -= 1

                    # add second to bottom row
                    if self.__arr__[r1 + 5][c1 + i] == 1:
                        count += 1
                    if self.__arr__[r1 + 6][c1 + i] == 1:
                        count += 1

                if count <= 2:
                    num_under_two += 1

        return num_under_two

    def num_horz_walls(self):
        count = 0
        # vertical
        for r in range(1, self.n, 2):
            a = []
            for c in range(0, self.m, 2):
                if self.__arr__[r][c] == 1:
                    count += 1
        return count

    def num_vert_walls(self):
        count = 0
        # vertical
        for r in range(0, self.n, 2):
            a = []
            for c in range(1, self.m, 2):
                if self.__arr__[r][c] == 1:
                    count += 1
        return count

    def count_all_shortest_loops_metric(self):
        pm = PathManager(self)

        cum = 0
        biggest_shortest_loop = (-1, -1, 0)
        for r in range(self.rows):
            for c in range(self.cols):
                v = pm.get_shortest_loop(r, c)
                if v > biggest_shortest_loop[2]:
                    biggest_shortest_loop = (r, c, v)
                cum += v
        return cum

    def __is_basic_six_metric__(self, r, c, k):
        num = (k-1) // 2
        # horizontal
        return self.__is_basic_horz__(r, c, num), self.__is__basic_vert__(r, c, num)

    def __is_basic_horz__(self, r, c, num):
        if not self.can_I_travel(r, c, 'D'):
            return False
        i = 0
        while i < num:
            if not self.can_I_travel(r, c + i, 'R'):
                return False
            i += 1
        if not self.can_I_travel(r, c + i, 'D'):
            return False
        while i >= 1:
            if not self.can_I_travel(r + 1, c + i, 'L'):
                return False
            i -= 1
        return True

    def __is__basic_vert__(self, r, c, num):
        if not self.can_I_travel(r, c, 'R'):
            return False
        i = 0
        while i < num:
            if not self.can_I_travel(r + i, c, 'D'):
                return False
            i += 1
        if not self.can_I_travel(r + i, c, 'R'):
            return False
        while i >= 1:
            if not self.can_I_travel(r + i, c + 1, 'U'):
                return False
            i -= 1
        return True

    def __get_all_dead_ends__(self):
        list1 = []
        for r in range(self.rows):
            for c in range(self.cols):
                neighbors = self.get_neighbors(r, c)
                if len(neighbors) == 1:
                    list1.append((r, c))
        return list1

    # used in generate_random_maze
    def __flood__(self, st_r=3, st_c=3):
        # keep track of every visited node
        # start at the beginning of the maze. go down every path (ignoring any cell that's been visited), marking each
        #   cell as visited as you go.
        # Check if every cell has been visited. If any haven't, return false
        pm = PathManager(self)
        return pm.flood(st_r, st_c)

    def __init_empty_arr__(self, n, m):
        a = [[0 for _ in range(self.m)] for _ in range(self.n)]
        for row in range(self.n):
            for col in range(self.m):
                if (row + col) % 2 == 0:
                    a[row][col] = -1

                # delete
                # if random.randint(1, 10) >= 8:
                #     a[row][col] = 1
        return a

    def __get_all_passages__(self):
        a = []
        for row in range(self.n):
            for col in range(self.m):
                if (row + col) % 2 == 1 and self.__arr__[row][col] == 0:
                    a.append([row, col])
        return a

    # all in matrix coordinates
    def __remove_random_wall__(self, r1, c1):
        # order = (top, right, down, left)
        neighbors = __get_neighbors_array__()
        # repeat until you find a wall
        rand_ind = random.randint(0, 3)

        while not (0 <= r1 + neighbors[rand_ind][0] < self.n and 0 <= c1 + neighbors[rand_ind][1] < self.m and self.__arr__[r1 + \
                neighbors[rand_ind][0]][c1 + neighbors[rand_ind][1]] != 0):
            rand_ind = random.randint(0, 3)

        r1_upd = r1 + neighbors[rand_ind][0]
        c1_upd = c1 + neighbors[rand_ind][1]

        self.__arr__[r1_upd][c1_upd] = 0

    # calculating if locaiton is a square using r, c as bottom right location
    def __is_square__(self, r, c):
        # check walls (quadrants): 1-2, 1-3, 2-4, 3-4
        r1, c1 = __convert_coor__(r, c)
        if r1 == 0 or c1 == 0:
            return False

        if self.__arr__[r1-2][c1-1] == 1:   # 1-2
            return False
        if self.__arr__[r1-1][c1-2] == 1:   # 1-3
            return False
        if self.__arr__[r1-1][c1] == 1:     # 2-4
            return False
        if self.__arr__[r1][c1-1] == 1:     # 3-4
            return False
        return True

