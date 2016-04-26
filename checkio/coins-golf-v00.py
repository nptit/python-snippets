# 76p 167th place
import itertools
def golf(l):
    n=len(l)+1
    l = sorted(set([sum(c) for r in range(1,n) for c in itertools.combinations(l,r)]))
    print l
    for i,x in enumerate(l):
        if i+1 != x: return i+1
    return l[-1]+1
