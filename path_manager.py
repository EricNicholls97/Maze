import copy

class PathManager:
    def __init__(self, matrix):
        self.matrix = matrix

    def flood(self, st_r, st_c):
        paths = [self.Path(st_r, st_c)]
        visited = [[0 for _ in range(self.matrix.nrows)] for _ in range(self.matrix.ncols)]

        while len(paths) > 0:
            p = paths.pop()
            visited[p.r][p.c] = 1

            for el in self.matrix.get_neighbors(p.r, p.c):
                rn = el[0]
                cn = el[1]
                if visited[rn][cn] == 0:
                    paths.append(self.Path(rn, cn, 0, p))

        for row in range(self.matrix.nrows):
            for col in range(self.matrix.ncols):
                if visited[row][col] == 0:
                    return False
        return True

    # TODO
    def get_shortest_loop(self, r, c):
        mp = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

        paths = [self.Path(r, c)]

        visited = [[False for _ in range(self.matrix.ncols)] for _ in range(self.matrix.nrows)]

        while len(paths) > 0:
            path = paths.pop(0)
            if path.val > 0 and path.r == r and path.c == c:
                return path.val

            new_r, new_c = path.r + mp['L'][0], path.c + mp['L'][1]
            if self.matrix.can_I_travel(path.r, path.c, 'L') and not path.is_prev(new_r, new_c):
                paths.append(self.Path(new_r, new_c, path.val + 1, path))

            new_r, new_c = path.r + mp['R'][0], path.c + mp['R'][1]
            if self.matrix.can_I_travel(path.r, path.c, 'R') and not path.is_prev(new_r, new_c):
                paths.append(self.Path(new_r, new_c, path.val + 1, path))

            new_r, new_c = path.r + mp['D'][0], path.c + mp['D'][1]
            if self.matrix.can_I_travel(path.r, path.c, 'D') and not path.is_prev(new_r, new_c):
                paths.append(self.Path(new_r, new_c, path.val + 1, path))

            new_r, new_c = path.r + mp['U'][0], path.c + mp['U'][1]
            if self.matrix.can_I_travel(path.r, path.c, 'U') and not path.is_prev(new_r, new_c):
                paths.append(self.Path(new_r, new_c, path.val + 1, path))

            if not (path.r == r and path.c == c):
                visited[path.r][path.c] = True

        return -1

    class Path:
        def __init__(self, r, c, val=0, prev=None):
            self.r = r
            self.c = c
            self.val = val
            self.prev = prev

        def __str__(self):
            return str(self.r) + ", " + str(self.c)

        def is_prev(self, r, c):
            if self.prev is None:
                return False

            return self.prev.r == r and self.prev.c == c

