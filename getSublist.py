
def getSublists(l, n):
    '''This function returns a list of all possible sublists in L of length n without skipping elements in L. The sublists in the returned list should be ordered in the way they appear in L, with those sublists starting from a smaller index being at the front of the list.'''
    nlen = len(l)
    if not (0 < n <= nlen):
        raise ValueError("Incorrect input value n: out of bound")
    if not l:
        raise ValueError("Empty list as input not allowed.")
    res = []
    for i in range(0, nlen-n+1):
        x = l[i:i+n]
        res.append(x)
    return res

print getSublists([1], 1)
print getSublists([10, 4, 6, 8, 3, 4, 5, 7, 7, 2], 4)
print getSublists([1, 1, 1, 1, 4], 2)
print getSublists([0, 0, 0, 0, 0], 2)
print getSublists([5, 2, 4, 1, 3], 1)
