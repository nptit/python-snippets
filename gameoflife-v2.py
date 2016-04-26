import sys
import numpy as np
from collections import Counter


class GameOfLife(object):
    def __xylim(self, tuples):
        """ Given positions of cells, find the minimum rectangle to
        cover those cells, represented by [(xmin,ymin), (xmax, ymax)]
        """

        # assume random ordering of tuples, otherwise, sort by y is not needed
        tuples_sorty = sorted(tuples, key=lambda x: x[1])
        ymin = tuples_sorty[0][1]
        ymax = tuples_sorty[-1][1]

        tuples_sortx = sorted(tuples, key=lambda x: x[0])
        xmin = tuples_sortx[0][0]
        xmax = tuples_sortx[-1][0]
        return [(xmin, xmax), (ymin, ymax)]

    def __mat2tuples(self, matrix):
        """ Given cells represented in a matrix, return a list of
        positions (i,j) with live cells"""

        return [(i, j) for i, row in enumerate(matrix)
                for j, col in enumerate(row) if col]

    def __tuples2minmat(self):
        """ Given positions of live cells (as x,y tuples), convert them in a
        minimum matrix representation"""
        if not self.data:
            return [[]], 0, 0

        (xmin, xmax), (ymin, ymax) = self.__xylim(self.data)
        ny = ymax - ymin + 1
        nx = xmax - xmin + 1
        matrix = [[0] * ny for _ in range(nx)]
        for t in self.data:
            x = t[0] - xmin
            y = t[1] - ymin
            matrix[x][y] = 1

        return matrix, xmin, ymin

    def __init__(self, data=None, m=5, n=5, seed=1,
                 percent_alive=0.5, boundary='periodic'):
        """ Initialize the game from a user supplied 2D matrix or
        random generated 2D matrix

        :param data: 2D matrix with values 1 or 0
        :param m: num of rows
        :param n: num of cols
        :param seed: seed for generating random number
        :return: a list of tuples, each tuple (x,y)
            corresponds to a cell with value 1
        """

        if not data:
            np.random.seed(seed)
            mat_data = np.random.choice(2, m * n,
                                        p=[1 - percent_alive, percent_alive]).reshape(m, n)
            self.m = m
            self.n = n
        else:
            mat_data = np.array(data)
            self.m = len(data)
            self.n = len(data[0])

        self.data = self.__mat2tuples(mat_data)
        self.start_state = mat_data
        if boundary in ('fixed', 'periodic', 'infinite'):
            self.boundary = boundary
        else:
            raise Exception('unknown boundary condition')

    def __neighbor_list(self, position):
        """ given a cell position (a tuple), return a list of indices of valid cells,
        based on boundary condition """

        assert isinstance(position, tuple)
        x, y = position
        m = self.m
        n = self.n
        mode = self.boundary

        nxy = lambda x, y: [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                            (x, y - 1), (x, y + 1), (x + 1, y - 1),
                            (x + 1, y), (x + 1, y + 1)]
        if mode == 'periodic':
            return [(i % m, j % n) for i, j in nxy(x, y)]
        elif mode == 'fixed':
            valid_pix = lambda x, y, m, n: 0 <= x < m and 0 <= y < n
            return [(a, b) for a, b in nxy(x, y) if valid_pix(a, b, m, n)]
        else:
            return nxy(x, y)

    def __count_live_neighbors(self, position):
        """ given a position, count how many its neighbors are alive  """

        return len(set(self.__neighbor_list(position)) & set(self.data))

    def __iter__(self):
        return self

    def next(self):
        """ one generation of evolution """

        if not self.data:
            return self

        # pass 1 check all live cells in current generation, and collect all neighboring dead cells
        new_gen = list()
        dead_neighbor_cells = list()

        for cell in self.data:
            dead_neighbor_cells.extend([t for t in self.__neighbor_list(cell)
                                        if t not in self.data])
            if 2 <= self.__count_live_neighbors(cell) <= 3:
                new_gen.append(cell)

        # pass 2, check dead cells adjacent to current live cells
        for cell in set(dead_neighbor_cells):
            if self.__count_live_neighbors(cell) == 3:
                new_gen.append(cell)

        # order the output by y, then by x
        self.data = sorted(new_gen, key=lambda x: (x[1], x[0]))
        return self

    def n_alive(self):
        return len(self.data)

    def __str__(self):
        # convert it into a matrix
        out = list()
        dim_old = "Original dimension ({},{}): ".format(self.m, self.n)
        matrix, xmin, ymin = self.__tuples2minmat()
        dim_new = "Current min matrix size ({},{}), xmin={}, ymin={} "\
            .format(len(matrix), len(matrix[0]), xmin, ymin)
        out.append("Header: {}\n{}\n".format(dim_old, dim_new))

        for row in matrix:
            out.extend(["1" if cell else "0" for cell in row])
            out.append("\n")

        return "".join(out)


if __name__ == "__main__":
    # example 1
    # mat = [[0, 1, 1], [1, 0, 1], [0, 1, 0]]
    # game = GameOfLife(data=mat, boundary='periodic')
    # print game
    # print game.next()
    # print game
    # sys.exit()

    # example 2

    gol_fixed = GameOfLife(m=20, n=20, percent_alive=0.5, seed=4, boundary='fixed')
    gol_periodic = GameOfLife(m=20, n=20, percent_alive=0.5, seed=4, boundary='periodic')
    gol_infinite = GameOfLife(m=20, n=20, percent_alive=0.5, seed=4, boundary='infinite')

    for _ in xrange(100):
        gol_fixed.next()
        gol_periodic.next()
        gol_infinite.next()

    print gol_fixed.n_alive()
    print gol_periodic.n_alive()
    print gol_infinite.n_alive()


    sys.exit()

    out = list()
    for i in xrange(500):
        ng = game.next().n_alive
        out.append(ng)

        # if the n_alive does not change for the 10 latest generation, stop
        if len(out) >= 10 and len(Counter(out[-10:])) == 1:
            break
    print out

    sys.exit()

    # for i in xrange(50):
    #     g = game.next()
    #     if not (i + 1) % 10:
    #         print "game ", i + 1, g
    #
    # ## example 3
    # giter = iter(g)
    # for i in giter:
    #     print i
    #     break
