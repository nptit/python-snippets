__author__ = 'qxu'

'''
Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.

The rules of the game are: 1. Any live cell with fewer than two live neighbours dies, as if
caused by underpopulation. 2. Any live cell with more than three live neighbours dies, as if by
overcrowding. 3. Any live cell with two or three live neighbours lives on to the next generation.
4. Any dead cell with exactly three live neighbours becomes a live cell.

Each cell's neighborhood is the 8 cells immediately around it. The universe is infinite
in both the x and y dimensions and all cells are initially dead - except for those specified in the
arguments. The return value should be a 2d array cropped around all of the living cells.
(If there are no living cells, then return [[]].)

For illustration purposes, 0 and 1 will be represented as ?? and ?? blocks respectively. You can
take advantage of the htmlize function to get a text representation of the universe: eg:

print htmlize(cells)

NB for unlimited boundary, we need to expand the border by one cell in each direction

'''

def mat2tuples(cells):
    """ Given cells represented in a matrix, return a list of positions (i,j) with live cells"""
    return [(i, j) for i, row in enumerate(cells) for j, col in enumerate(row) if col]

def tuples2mat(tuples):
    """ Given positions of live cells (as x,y tuples), convert them in a minimum matrix representation"""
    if not tuples:
        return [[]]

    (xmin, xmax), (ymin, ymax) = xylim(tuples)
    ny = ymax - ymin + 1
    nx = xmax - xmin + 1
    mat = [[0]*ny for _ in range(nx)]
    for t in tuples:
        x = t[0] - xmin
        y = t[1] - ymin
        mat[x][y] = 1
    return mat


def xylim(tuples):
    """ Given positions of live cells, find the minimum rectangle to cover those cells, represented by
    (xmin,ymin), (xmax, ymax)
    """
    # assume random ordering of tuples, otherwise, sort by y is not needed
    tuples_sorty = sorted(tuples, key=lambda x: x[1])
    ymin = tuples_sorty[0][1]
    ymax = tuples_sorty[-1][1]

    tuples_sortx = sorted(tuples, key=lambda x: x[0])
    xmin = tuples_sortx[0][0]
    xmax = tuples_sortx[-1][0]
    return [(xmin, xmax), (ymin, ymax)]


def get_neighbors(t):
    x, y = t
    return [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
            (x, y - 1), (x, y + 1), (x + 1, y - 1),
            (x + 1, y), (x + 1, y + 1)]


def count_live_neighbors(position_tuple, all_live_tuples):
    """ given a tuple, count how many its neighbors are alive  """
    return len(set(get_neighbors(position_tuple)) & set(all_live_tuples))


def one_generation(all_live_tuples):
    """ one generation of evolution by rule """
    if not all_live_tuples:
        return []

    # pass 1 check all live cells in current generation, and collect all neighboring dead cells
    new_gen = list()
    dead_neighbor_cells = list()
    for cell in all_live_tuples:
        dead_neighbor_cells.extend([t for t in get_neighbors(cell) if t not in all_live_tuples])
        if 2 <= count_live_neighbors(cell, all_live_tuples) <= 3:
            new_gen.append(cell)

    # pass 2, check dead cells adjacent to current live cells
    for cell in set(dead_neighbor_cells):
        if count_live_neighbors(cell, all_live_tuples) == 3:
            new_gen.append(cell)

    # order the output by y, then by x
    return sorted(new_gen, key=lambda x: (x[1], x[0]))


def evolve(all_live_tuples, ngenerations):
    """ evolve a specific generations """
    curr = all_live_tuples
    for _ in range(ngenerations):
        curr = one_generation(curr)
    return curr


def get_generation(cells, generations):
    """ Provide matrix interface """
    tuples = mat2tuples(cells)
    new_gen = evolve(tuples, generations)
    return tuples2mat(new_gen)

if __name__ == '__main__':
    start = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]
    t = mat2tuples(start)
    print t
    one = one_generation(t)
    five = evolve(t, 15)
    print tuples2mat(one)
    print tuples2mat(five)