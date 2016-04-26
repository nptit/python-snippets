import math
from collections import Counter

def checkio(radius):
    """given a radius of a circle, count minimum squares of length 1
    needed to completely cover the circle and count how many fall within it"""
    # since the geometry is 4 fold symmetric, we only need to consider one quadrant
    xmax = int(math.ceil(radius))

    # method: we can keep two corners (lower left, and upper right) of each square,
    # and check whether both corner is inside the circle (full), or one corner
    # inside the circle (partial)
    corners = [((i, j), (i + 1, j + 1)) for i in range(0, xmax) for j in range(0, xmax)]
    inside = lambda x: x[0]**2 + x[1]**2 <= radius**2
    c = Counter([inside(x) + inside(y) for x,y in corners])
    return [c[2]*4, c[1]*4]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"
