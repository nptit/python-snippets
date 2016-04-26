'''  Nikola picks up a strange circuit board. All of its elements are connected
in a spiral and it is possible to connect the neighboring elements vertically
and horizontally.

The map of the circuit consists of a series of square cells. The first element
in the center is marked as 1, and continuing in a clockwise spiral, each other
elements is marked in ascending order. On the map, you can move (connect cells)
vertically and horizontally. You can help Nikola find the manhattan distance
between any two elements on the map. For example, the distance between cells 1
and 9 is two moves and the distance between 24 and 9 is one move.


find_distance(1, 9) == 2

find_distance(9, 1) == 2

find_distance(10, 25) == 1

find_distance(5, 9) == 4'''


def upleft(layer):
    'give coordinates of the upper left corner of a layer'
    return -layer, layer

import math
def layer(k):
    'given a number, find which layer it is on: (2n-1)**2 < k <= (2n+1)**2, layer start from 0'
    sqrtk = k**0.5
    lower_bound = (sqrtk - 1) / 2
    # upper_bound = (sqrtk + 1) / 2
    return int(math.ceil(lower_bound))

def coord(n):
    'given n found its coordinates i, j'
    if n == 1:
        return 0, 0

    l = layer(n)
    start = (2 * l - 1) **2 + 1
    end = (2 *l + 1)**2
    x = -l
    y = l
    nedge = 2 * l + 1
    for i in range(start, end + 1):
        if i <  start + nedge -1:
            x += 1
        elif i < start + 2 * (nedge -1):
            y -= 1
        elif i < start + 3 * (nedge -1):
            x -= 1
        else:
            y += 1
        if i == n:
            return x, y
    raise Exception("Incorrect algorithm")


def find_distance(startp,endp):
    x1, y1 = coord(startp)
    x2, y2 = coord(endp)
    return abs(x1 - x2) + abs(y1 - y2)

print find_distance(1,9)
