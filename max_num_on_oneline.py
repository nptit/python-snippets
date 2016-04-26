__author__ = 'qxu'

from collections import defaultdict


class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

from collections import Counter

class Solution:
    # Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
    # @param {int[]} points an array of point
    # @return {int} an integer

    def maxPoints(self, points):
        # points=[ (p.x, p.y) for p in points]
        np = len(points)
        maxnp = 0
        for i in xrange(np):
            result = []
            dup = 0
            x1, y1 = points[i]
            for j in xrange(i + 1, np):
                x2, y2 = points[j]
                diffx = x2-x1
                diffy = y2-y1
                if abs(diffx)+abs(diffy) < 1.e-8:
                    dup += 1
                    break
                    print i, "=", j
                elif abs(diffx) > 1.e-8:
                    slope = diffy / float(diffx)
                    result.append(slope)
                else:
                    slope = float('inf')
                    result.append(slope)

            nslope = Counter(result).most_common(1)
            print np, i, j, result, len(result), dup, nslope
            if len(nslope) < 1:
                maxnp_update = dup + 1
            else:
                maxnp_update = nslope[0][1] + dup+1
            if maxnp < maxnp_update:
                maxnp = maxnp_update

        return maxnp

points = [(1, 2), (3, 6), (0, 0), (1, 3)]
points = [[1, 2], [3, 6], [0, 0], [1, 3]]  # 3
points = [[0, 0], [1, 1], [1,-1], [1, -1], [1,1]]  # 2
points = [[0, -12], [5, 2], [2, 5], [0, -5], [1, 5], [2, -2], [5, -4], [3, 4], [-2, 4], [-1, 4], [0, -5], [0, -8],
          [-2, -1], [0, -11], [0, -9]]  # 6
points = [[1,1],[1,1],[1,1],[2,2]]
points = [[0,9],[138,429],[115,359],[115,359],[-30,-102],[230,709],[-150,-686],[-135,-613],[-60,-248],[-161,-481],[207,639],[23,79],[-230,-691],[-115,-341],[92,289],[60,336],[-105,-467],[135,701],[-90,-394],[-184,-551],[150,774]]

s = Solution()
print s.maxPoints(points)
