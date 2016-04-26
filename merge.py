def merge(l1, l2):
    '''merge two incrementally sorted list'''
    res = []
    while l1 and l2:
        if l1[0] >= l2[0]:
            res.append(l2.pop(0))
        else:
            res.append(l1.pop(0))

    if l1:
        res.extend(l1)
    else:
        res.extend(l2)
    return res


def removeDup(l):
    '''Given a sorted array, remove the duplicates in place such that each element appear only once
and return the new length.'''
    if not l:
        return 0
    n = 0
    for i,v in enumerate(l[:-1]):
        if v != l[i+1]:
            n += 1

    return n+1

print removeDup([1,1,2, 2,3, 3, 3, 3, 4])
print removeDup([])
