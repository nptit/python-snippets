__author__ = 'qxu'

'''
Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.

The rules of the game are: 1. Any live cell with fewer than two live neighbours dies, as if
caused by underpopulation. 2. Any live cell with more than three live neighbours dies, as if by
overcrowding. 3. Any live cell with two or three live neighbours lives on to the next generation.
4. Any dead cell with exactly three live neighbours becomes a live cell.

In this implementation, the size of the region is fixed.

'''


# the following implementation first considers the area is bounded

# for unlimited boundary, we need to consider expand the border by one cell in each direction

def neighbor_list(index, m, n):
    ''' given a cell position (a tuple) and cell dimensions, return a list of indices of valid cells '''
    x, y = index
    nxy = lambda x, y: [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y),
                        (x + 1, y + 1)]
    valid_pix = lambda x, y, m, n: 0 <= x <= m - 1 and 0 <= y <= n - 1
    return [(a, b) for a, b in nxy(x, y) if valid_pix(a, b, m, n)]


def update_by_rule(value, live_neighbours):
    ''' give a value and its number of live neighbors, return a new value based on a set of rules    '''
    if value == 1:
        # under population or overpopulation
        if live_neighbours < 2 or live_neighbours > 3:
            return 0
        else:
            return 1
    # offspring
    if value == 0 and live_neighbours == 3:
        return 1
    return value


def count_live_neighbors(cells, indices):
    ''' sum up the cell values for given indices (given as tuples) '''
    return sum(cells[i][j] for i, j in indices)


def one_generation(cells):
    ''' one generation of evolution by rule '''
    m = len(cells)  # mrows
    n = len(cells[0])  # ncols
    new_cells = [[0] * n for _ in range(m)]
    for i in xrange(m):
        for j in xrange(n):
            nlive_neighbors = count_live_neighbors(cells, neighbor_list((i, j), m, n))
            new_cells[i][j] = update_by_rule(cells[i][j], nlive_neighbors)
    return new_cells


def get_generation(cells, generations):
    for _ in xrange(generations):
        cells = one_generation(cells)
    return cells


if __name__ == '__main__':
    start = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    x = one_generation(start)

    assert (x == start)

    import numpy as np
    print np.array(x)
