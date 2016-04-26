from timeit import timeit, Timer

from bisect import bisect_left
def binary_search(a, x, lo=0, hi=None):
    hi = hi or len(a)
    # find insertion position
    pos = bisect_left(a, x, lo, hi)
    return (pos if pos != hi and a[pos] == x else -1)

def twosum_bisearch(nums,t):
    '''about 5 time slower than set lookup'''
    for s in nums:
        if binary_search(nums, t-s) != -1 and s != t-s :
            return 1
    return 0

def twosum_set(nums, t):
    '''look up in set/hash is very slow in this case...why?'''
    for s in nums:
      if t-s in nums and s != t-s:
        return 1
    return 0

def twosum_set_str(nums, t):
    '''look up in set is very slow in this case...why?
    str as key does not improve run time for set'''
    for s in nums:
        if t - int(s) in nums and int(s) != t - int (s):
            return 1
    return 0


def test1(lines):
    return sum([twosum_bisearch(lines, t) for t in range(5)])

def test2(nums):
    return sum([twosum_set(nums, t) for t in range(5)])

def test3(strs):
    return sum([twosum_set_str(strs, t) for t in range(5)])

def test4(nums_dict):
    return sum([twosum_set(nums_dict, t) for t in range(5)])

def test5(nums_ddict):
    return sum([twosum_set(nums_ddict, t) for t in range(5)])

from collections import defaultdict
if __name__ == '__main__':
    lines = [int(line.rstrip('\n')) for line in open('algo1_programming_prob_2sum.txt')]
    nums = set(lines)
    strs = set([line.rstrip('\n') for line in open('algo1_programming_prob_2sum.txt')])
    nums_dict = dict([(i, None) for i in nums])
    nums_ddict = defaultdict(None)
    for i in nums:
        nums_ddict[i] = None

    print "done read data."

    '''
    # extremely slow for two calls below
    results = [twosum_bisearch(lines,t) for t in range(-10000, 10001)]
    results = [ twosum_set(nums,t) for t in range(-10000, 10001)]
    '''

    print Timer(stmt='test1(sorted(lines))', setup='from __main__ import test1, twosum_bisearch, binary_search, lines').timeit(number=1)
    print Timer(stmt='test2(nums)', setup='from __main__ import test2, twosum_set, nums').timeit(number=1)
    print Timer(stmt='test3(strs)', setup='from __main__ import test3, twosum_set_str, strs').timeit(number=1)
    print Timer(stmt='test4(nums_dict)', setup='from __main__ import test4, twosum_set, nums_dict').timeit(number=1)
    print Timer(stmt='test5(nums_ddict)', setup='from __main__ import test5, twosum_set, nums_ddict').timeit(number=1)
    print "done"

