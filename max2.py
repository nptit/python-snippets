__author__ = 'qxu'

def max2(lst):
    # find max 2 number of an unsorted list
    if len(lst) < 2:
        return lst
    max1 = max(lst[1], lst[0])
    max2 = min(lst[1], lst[0])
    for i in xrange(2, len(lst)):
        if lst[i] > max1:
            max2 = min(max1, lst[i])
            max1 = max(max1, lst[i])
        elif max1 > lst[i] > max2:
            max2 = lst[i]
    return [max1, max2]

import heapq
def maxk(lst):
    # find k largest of smallest number using priority queue
    heapq.heapify(lst)
    return heapq.nlargest(2,lst)

lst=[11,1,2,4,5,8]

print max2(lst)
print maxk(lst)