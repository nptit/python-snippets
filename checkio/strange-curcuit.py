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
    positions = [(x, l) for x in range(-l+1, l+1)] + [(l, x) for x in range(l-1, -l-1, -1)] \
            + [(x, -l) for x in range(l-1, -l-1, -1)] + [(-l, x) for x in range(-l+1, l+1, 1)]
    return positions[n - start]

def find_distance(startp, endp):
    x1, y1 = coord(startp)
    x2, y2 = coord(endp)
    return abs(x1 - x2) + abs(y1 - y2)





# calculate the coordinate of n

def coord(n):

    if n == 1: return (0, 0)

    r = int(sqrt(n - 1) - 1) // 2 + 1

    g, d = divmod(n - (2*r-1)**2 - 1, 2*r)

    return [(-r+d+1, r), (r, r-d-1), (r-d-1, -r), (-r, -r+d+1)][g]

​

def find_distance(first, second):

    x1, y1 = coord(first)

    x2, y2 = coord(second)

    return abs(x2 - x1) + abs(y2 - y1)

​

    # At first, we determine ring which include n

    #   ring 0 : 1

    #   ring 1 : 2,3,...,9

    #   ring 2 : 10,11,...,25

    #   ring r : (2*r-1)**2+1,...,(2*r+1)**2

    # Using following formula, we can calculate r from n.

    #   r = int((sqrt(n - 1) - 1) / 2) + 1

    # Ring r have 8*r elements and start position is (-r+1, r).

    # And another interesting position is follows.

    #   (-r,  r) : left upper corner,  n = (2*r-1)**2 + 8*r = (2*r+1)**2

    #   ( r,  r) : right upper corner, n = (2*r-1)**2 + 2*r

    #   ( r, -r) : right lower corner, n = (2*r-1)**2 + 4*r

    #   (-r, -r) : left lower corner,  n = (2*r-1)**2 + 6*r

    #

    # Second, I divide ring into 4 groups corresponding to the direction.

    # Each group size is 2*r. The group 0 is the first 2*r elements of the ring

    # and its direction is right, and so on.

    #   group 0 (dir = R) : n is from (2*r-1)**2    +1 to (2*r-1)**2+2*r

    #   group 1 (dir = D) : n is from (2*r-1)**2+2*r+1 to (2*r-1)**2+4*r

    #   group 2 (dir = L) : n is from (2*r-1)**2+4*r+1 to (2*r-1)**2+6*r

    #   group 3 (dir = U) : n is from (2*r-1)**2+6*r+1 to (2*r-1)**2+8*r

    # Using following formula, we can calculate group number g from n, r.

    #   g = int((n - (2*r-1)**2 - 1) / (2*r)

    #

    # Finally, using above information, we will calulate the coordinate of n.

    # When n belongs to group 0 of ring r, then the coordinate of n is

    # (-r+1 + d, r), where d means n is the d-th elements of the group.

    # As well, we can calculate for another groups.

    #   group 0 : (-r+1+d, r)

    #   group 1 : (r, r-1+d)

    #   group 2 : (r-1-d, r)

    #   group 3 : (-r, -r+d+1)














if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_distance(1, 9) == 2, "First"
    assert find_distance(9, 1) == 2, "Reverse First"
    assert find_distance(10, 25) == 1, "Neighbours"
    assert find_distance(5, 9) == 4, "Diagonal"
    assert find_distance(26, 31) == 5, "One row"
    assert find_distance(50, 16) == 10, "One more test"
