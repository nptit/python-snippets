
def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print "sum(%s)=%s" % (partial, target)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])


#if __name__ == "__main__":
    #subset_sum([3,9,8,4,5,7,10],15)

    #Outputs:
    #sum([3, 8, 4])=15
    #sum([3, 5, 7])=15
    #sum([8, 7])=15
    #sum([5, 10])=15


import itertools
def golf(l):
    n=len(l)+1
    l = sorted(set([sum(c) for r in range(1,n) for c in itertools.combinations(l,r)]))
    print l
    for i,x in enumerate(l):
        if i+1 != x: return i+1
    return l[-1]+1



print golf([1,2,3]) == 7
print golf([9, 2, 2, 1]) == 6
print golf([1, 1, 1, 1]) == 5
print golf([1, 2, 3, 4, 5]) == 16

