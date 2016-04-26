
import random
def quickSelect(l, k):
    ''' return the kth smallest element in unordered list l'''

    if len(l) == 1:
        return l[0]

    pivot = random.choice(range(len(l)))
    la = [e for e in l if e < l[pivot ]]
    ra = [e for e in l if e >= l[pivot]]
    if k == len(la):
        return la[-1]
    elif k < len(la):
        return quickSelect(la, k)
    else:
        return quickSelect(ra, k - len(la))


print quickSelect([0, 5, 1, 3, 2,4], 6)
