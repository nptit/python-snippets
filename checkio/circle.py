from math import sqrt, acos, pi

def dist(p1, p2):
    'calculate distance between two points in 2D'
    x1, y1 = p1[0:2]
    x2, y2 = p2[0:2]
    return sqrt((x1 - x2)**2 + (y1 - y2) **2)

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
    term1 = r1**2 *acos ((d**2 + r1**2 - r2**2) / (2*d*r1))
    term2 = r2**2 *acos ((d**2 + r2**2 - r1**2) / (2*d*r2))

    min_area = min(area(r1), area(r2))
    return 100 * (term1 + term2 - 0.5 * d * a) / min_area

def merge_circles(c1, c2):
    'check whether two circles can be merged'
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    area1 = area(r1)
    area2 = area(r2)
    if area_intersect(c1, c2) >= 55:
        #area1 >= 1.2 * area2 or area2 >= 1.2 * area1:
        if abs(area1 - area2) / min(area1, area2) >= 0.2:
            'merge into c1'
            new_r = sqrt(r1**2 + r2**2)
            return (x1, y1, new_r)

    return None

def one_update(circles):
    state = circles[:]
    for i, c1 in enumerate(circles):
        disti = [(i+1, dist(c1, c2)) for c2 in circles[i+1:]]
        disti = sorted(disti, key = lambda x: x[1])
        for (j, _) in disti:
            c2 = circles[j]
            nc = merge_circles(c1, c2)
            if nc:
                state[i] = nc
                state.pop(j)
                return state

    return state



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

if __name__ == "__main__":
    print checkio([(0, 0, 2.1)]) #== [(0, 0, 2.1)]
    print checkio([(2, 4, 2), (3, 9, 3)]) #== [(2, 4, 2), (3, 9, 3)]
    print checkio([(3, 3, 3), (2, 2, 1), (3, 5, 1.5)]) #== [(3, 3, 3.5)]


