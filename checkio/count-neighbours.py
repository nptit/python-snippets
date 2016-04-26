def count_neighbours(grid, row, col):
    m, n = len(grid), len(grid[0])
    x, y = row, col

    nxy = lambda x, y: [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                        (x, y - 1), (x, y + 1), (x + 1, y - 1),
                        (x + 1, y), (x + 1, y + 1)]

    valid_cell = lambda x, y, m, n: 0 <= x < m and 0 <= y < n
    return sum([grid[a][b] for a, b in nxy(x, y) if valid_cell(a, b, m, n)])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(
        ((1, 0, 0, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 1, 0, 1),
         (1, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
