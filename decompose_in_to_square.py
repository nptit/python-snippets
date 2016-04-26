__author__ = 'qxu'

def decompose(n):
    def _recurse(s, i):
        if s < 0:
            return None
        if s == 0:
            return []
        for j in xrange(i-1, 0, -1):
            sub = _recurse(s - j**2, j)
            if sub != None:
                return sub + [j]
    return _recurse(n**2, n)


def decompose2(n):
    goal = 0
    result = [n]
    while result:
        current = result.pop()
        goal += current ** 2
        for i in range(current - 1, 0, -1):
            if goal - (i ** 2) >= 0:
                goal -= i ** 2
                result.append(i)
                if goal == 0:
                    result.sort()
                    return result
    return None

print decompose(50) # [1, 3, 5, 8, 49])
print decompose2(625)  # [2, 5, 8, 34, 624]#
