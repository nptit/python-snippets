def mat2tuples(cells):
    """ Given cells represented in a matrix, return a list of positions (i,j) with live cells"""
    return [(i, j) for i, row in enumerate(cells) for j, col in enumerate(row) if col]

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

def life_counter(state, tick_n):
    """ evolve a specific generations """
    curr = mat2tuples(state)
    for _ in range(tick_n):
        curr = one_generation(curr)
    return len(curr)

if __name__ == '__main__':
    assert life_counter(((0, 1, 0),
                         (0, 0, 1),
                         (1, 1, 1)), 50) == 5, "Glider"
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert life_counter(((0, 1, 0, 0, 0, 0, 0),
                         (0, 0, 1, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0)), 4) == 15, "Example"
    assert life_counter(((0, 1, 0, 0, 0, 0, 0),
                         (0, 0, 1, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0)), 15) == 14, "Little later"

    assert life_counter(((1, 1, 0, 1, 1),
                         (1, 1, 0, 1, 1),
                         (0, 0, 0, 0, 0),
                         (1, 1, 0, 1, 1),
                         (1, 1, 0, 1, 1)), 100) == 16, "Stones"
