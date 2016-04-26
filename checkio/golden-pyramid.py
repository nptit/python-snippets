def count_gold(data):
    'top to bottom dynamic programming, R(x,y) = max(R(x-1,y-1), R(x-1, y)) + v(x,y)'
    R = [[0]*len(row) for row in data]
    R[0][0] = data[0][0]

    for i, row in enumerate(data[1:], 1):
        for j, v in enumerate(row):
            if j == 0:
                R[i][j] = R[i-1][j] + v
            elif j == len(row) - 1:
                R[i][j] = R[i-1][j-1] + v
            else:
                R[i][j] = max(R[i-1][j-1], R[i-1][j]) + v

    return max(R[-1])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
