from itertools import combinations

def f(k, n, incr=0):
    if k >= n:
        return ','.join([''.join([str(i+incr) for i in range(n)])]*2)

    if n == k + 1:
        d = {i:2 for i in range(incr, incr + n)}
        r = []
        for c in combinations(range(incr, incr + n), k):
            l = []
            for x in c:
                if d[x] > 0:
                    l.append(str(x))
                d[x] -= 1
            if l: r.append(''.join(l))
        return ','.join(r)

    return ','.join([f(k, k, incr), f(k, n - k, incr + k)])

def choose(k, n):
    'choose k numbers from n in smallest steps such that each number can only be'
    'chosen twice, the same number cannot appear twice in one selection'
    d = {i:2 for i in range(n)}
    pass

print len(f(4,6))==3 #1234, 3456, 1256
print f(2,3)
print f(3,4)
