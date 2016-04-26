def ccw(pa, pb, pc):
    "give three points, check whether pa-pb-pc are counter clockwise"
    v = (pb[0] - pa[0]) * (pc[1] - pa[1]) - (pb[1] - pa[1]) * (pc[0] - pa[0])
    if v > 0:
        return 1 # CCW
    elif v < 0:
        return -1 # CW
    else:
        return 0 # colinear

def checkio(points):
    # brute force method O(n**3)
    hullpoints = set()
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points[i+1:], i+1):
            if all([ccw(p1, p2, p) for k, p in enumerate(points) if k not in (i,j)]):
                hullpoints.add(i)
                hullpoints.add(j)
    return list(hullpoints)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(
        [[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]
    ) == [4, 5, 6, 0, 1, 2, 3], "First example"
    assert checkio(
        [[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]
    ) == [1, 0, 6, 3, 5, 2], "Second example"
