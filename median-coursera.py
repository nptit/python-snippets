__author__ = 'qxu'

"""
Question 2
Download the text file here.

The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 5 lecture on heap
applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat
this as a stream of numbers, arriving one by one. Letting xi denote the ith number of the file, the kth median
mk is defined as the median of the numbers x1, ... ,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest number
among x1,... ,xk; if k is even, then mk is the (k/2)th smallest number among x1, ..., xk.)

In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits).
That is, you should compute (m1+m2+m3+...+m10000)mod10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations
of the algorithm.
"""

import heapq

def median_brute(lst):
    lst = sorted(lst)
    if len(lst) % 2 == 0:
        return lst[len(lst) / 2 - 1]
    return lst[(len(lst)+1) / 2 - 1]

def median_from_stream(nums):
    # keep track of median using two heaps
    if len(nums) == 2:
        return [nums[0], min(nums[:2])]
    elif len(nums) == 1:
        return [nums[0]]

    # intiallization
    heap1 = [max(nums[:2])] # upper bucket to keep track of min
    heap2 = [-min(nums[:2])] # lower bucket to keep track of max
    medians = [nums[0], min(nums[:2])]

    for i in nums[2:]:
        # push into an appropriate heap
        if i < -heap2[0]:
            heapq.heappush(heap2, -i)
        else:
            heapq.heappush(heap1, i)

        # re-balance if needed such that abs(len1-len2)<=1
        while len(heap1) - len(heap2) > 1:
            e = heapq.heappop(heap1)
            heapq.heappush(heap2, -e)

        while len(heap2) - len(heap1) > 1:
            e = heapq.heappop(heap2)
            heapq.heappush(heap1, -e)

        if len(heap1) <= len(heap2):
            medians.append(-heap2[0])
        elif len(heap1) > len(heap2):
            medians.append(heap1[0])

    return medians


if __name__ == '__main__':

    with open("Median.txt") as fh:
        lines = fh.readlines()

    nums = [int(l.rstrip()) for l in lines]

    medians = median_from_stream(nums)
    print "result (heap) =", sum(medians) % 10000

    #print "result (sort) =", sum([median_brute(nums[:i+1]) for i in xrange(len(nums))]) % 10000