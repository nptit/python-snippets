def ccw(pa, pb, pc):
    "give three points, check whether pa-pb-pc are counter clockwise"
    v = (pb[0] - pa[0]) * (pc[1] - pa[1]) - (pb[1] - pa[1]) * (pc[0] - pa[0])
    if v > 0:
        return 1 # CCW
    elif v < 0:
        return -1 # CW
    else:
        return 0 # colinear

def bf_convex_hull(points):
    # brute force method O(n**3)
    print points
    hullpoints = []
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points[i+1:], i+1):
            if all([ccw(p1, p2, p) == -1 for p in points if p not in (p1, p2)]):
                print "accept p1 and p2"
                if i not in hullpoints:
                    hullpoints.append(i)
                if j not in hullpoints:
                    hullpoints.append(j)
            for p in points:
                if p != p1 and p != p2:
                    ccwx = ccw(p1, p2, p)
                    print i, j, p1, p2, "p=",p, ccwx
                # if p == p1 or p == p2:
                #     pass
                # else:
                #     ccwx = ccw(p1, p2, p)
            print "\n"

    return hullpoints

#print bf_convex_hull([[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]])
print bf_convex_hull([[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]])
