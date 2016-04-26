__author__ = 'qxu'

from math import sqrt, acos, pi


def dist(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def area(r):
    'area of a circle with radius r'
    return pi * r**2

def area_intersect(c1, c2):
    'calculate intersection area between two circles --given as (x, y, r) tuples'
    'return as a percentage of the smaller area: 0 - 100 percent'
    'see http://mathworld.wolfram.com/Circle-CircleIntersection.html'
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    d = dist(c1, c2)

    if d <= max(r1, r2) - min(r1, r2):
        return 100
    elif d >= r1 + r2:
        return 0

    a = sqrt((-d + r1 - r2) * (-d - r1 + r2) * (-d + r1 + r2) * (d + r1 + r2)) / d
    term1 = r1**2 * acos((d**2 + r1**2 - r2**2) / (2*d*r1))
    term2 = r2**2 * acos((d**2 + r2**2 - r1**2) / (2*d*r2))

    min_area = min(area(r1), area(r2))
    return 100 * (term1 + term2 - 0.5 * d * a) / min_area

def merge_circles(c1, c2):
    'check whether two circles can be merged'
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    area1 = area(r1)
    area2 = area(r2)
    if area_intersect(c1, c2) >= 55:
        # if abs(area1 - area2) / min(area1, area2) >= 0.2:
        #     'merge into c1'
        #     new_r = sqrt(r1**2 + r2**2)
        #     return (x1, y1, new_r)
        new_r = sqrt(r1**2 + r2**2)
        if area1 >= 1.2 * area2:
            return 1, (x1, y1, new_r)
        elif area2 >= 1.2 * area1:
            return 2, (x2, y2, new_r)

    return None, None

def one_update(circles):
    'straightforward but poor performance'
    new = circles[:]
    nc = len(circles)
    distij = [(True, i, j, dist(circles[i], circles[j])) for i in range(nc) for j in range(i+1, nc)]
    distij = sorted(distij, key=lambda (s, i, j, d): (d, i))

    for t in distij:
        status, i, j, d = t
        c1 = circles[i]
        c2 = circles[j]
        which, nc = merge_circles(c1, c2)
        if nc:
            if which == 1:
                new[i] = nc
                new.pop(j)
            else:
                new[j] = nc
                new.pop(i)
            return new

    return new


def checkio(circles):
    if len(circles) == 1:
        return circles

    input = circles[:]
    while True:
        out = one_update(input)
        if out == input:
            func = lambda (x, y, r): (x, y, round(r, 2)) if isinstance(r, float) else (x, y, r)
            return map(func, out)
        else:
            input = out[:]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    c1 = (2, 2, 3)
    c2 = (0, 4, 2)
    #print dist(c1, c2), area(c1[2]), area(c2[2]), area_intersect(c1, c2)*area(c2[2])/100
    c1 = (0.8, 0, 1)
    c2 = (1, 0, 1.118033988749895)
    #print dist(c1, c2), area(c1[2]), area(c2[2]), area_intersect(c1, c2)
    #print one_update([(0.8, 0, 1), (1, 0, 1.12)])

    print checkio([(0.8, 0, 1), (1, 0, 1),(1.5, 0, 0.5)]) # == [(1,0,1.5)]

    assert checkio([(2, 4, 2), (3, 9, 3)]) == [(2, 4, 2), (3, 9, 3)]
    assert checkio([(0, 0, 2), (-1, 0, 2)]) == [(0, 0, 2), (-1, 0, 2)]
    assert checkio([(4, 3, 2), (2.5, 3.5, 1.4)]) == [(4, 3, 2.44)]
    assert checkio([(3, 3, 3), (2, 2, 1), (3, 5, 1.5)]) == [(3, 3, 3.5)]
