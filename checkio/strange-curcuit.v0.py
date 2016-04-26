import math
def layer(k):
    'given a number, find which layer it is on: (2n-1)**2 < k <= (2n+1)**2, layer start from 0'
    sqrtk = k**0.5
    lower_bound = (sqrtk - 1) / 2
    return int(math.ceil(lower_bound))

def coord(n):
    'given n find its coordinates x, y'
    if n == 1:
        return 0, 0

    l = layer(n)
    start = (2 * l - 1) **2 + 1
    end = (2 *l + 1)**2
    # upper left corner, containing the last value for this layer
    x = -l
    y = l
    nedge = 2 * l + 1 # numbers per edge

    # this part needs improvement
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

def coord(n):
    'given n find its coordinates x, y'
    if n == 1:
        return 0, 0

    l = layer(n)
    start = (2 * l - 1) **2 + 1
    positions = [(x, l) for x in range(-l+1, l+1)] + [(l, x) for x in range(l-1, -l-1, -1)] \
            + [(x, -l) for x in range(l-1, -l-1, -1)] + [(-l, x) for x in range(-l+1, l+1, 1)]

    return positions[n - start]

def find_distance(startp, endp):
    x1, y1 = coord(startp)
    x2, y2 = coord(endp)
    return abs(x1 - x2) + abs(y1 - y2)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_distance(1, 9) == 2, "First"
    assert find_distance(9, 1) == 2, "Reverse First"
    assert find_distance(10, 25) == 1, "Neighbours"
    assert find_distance(5, 9) == 4, "Diagonal"
    assert find_distance(26, 31) == 5, "One row"
    assert find_distance(50, 16) == 10, "One more test"
