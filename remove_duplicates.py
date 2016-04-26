def dedup(l1):
    '''remove duplicates from sorted array, return the new length'''
    n = len(l1)

    newidx = 0
    for i in range(1, n):
        if l[i] != l[newidx]:
            newidx += 1
            l[newidx] = l[i]
    return newidx+1 if n else 0


l = [1, 1, 2, 2]
l = []
print dedup(l), l[:dedup(l)]


def find_mode(l):
    '''given a list, found the mode---most common occuring number'''
    import collections
    return collections.Counter(l).most_common(1)[0][0]

print find_mode([1,1,1, 2, 2,2, 2])

def find_mode(l):
    d = {}
    for e in l:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1

    print max(d, key = d.get)
    print max(d, key = lambda key: (d[key], -key))

find_mode([1,1,1, 2, 2,2])

