__author__ = 'qxu'

import math


def partition1(arr):
    # partition using first element of arr
    p = arr[0]
    i = 1

    for j in range(i, len(arr)):
        if arr[j] < p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[0], arr[i-1] = arr[i-1], arr[0]

    return arr[0:i-1], arr[i-1], arr[i:len(arr)]


def partition2(arr):
    # partition using the last element of arr
    # swapping first and last element
    arr[0],arr[-1]=arr[-1],arr[0]

    return partition1(arr)



def partition3(arr):
    # partition using middle of the three
    # middle of three
    start = arr[0]
    last = arr[-1]
    m = (len(arr)+1) // 2 - 1
    middle = arr[m]

    d = dict([(start, 0), (last, -1), (middle, m)])
    mx = d[sorted(d.keys())[1]]
    #print "mx=", mx, "m=", m, d

    # swapping first and whatever index corresponding to the middle
    arr[0], arr[mx] = arr[mx], arr[0]

    return partition1(arr)



def qsort(arr):
    global ncmp

    if len(arr) <= 1:
        return arr

    # first element as pivot
    method = 'm3'
    if method == 'first':
        less, eq, more = partition1(arr)
    # the last element as pivot
    elif method == 'last':
        less, eq, more = partition2(arr)
    elif method == 'm3':
        less, eq, more = partition3(arr)

    ncmp += len(arr) - 1
    return qsort(less) + [eq] + qsort(more)


if __name__ == '__main__':

    a = [3, 8, 2, 5, 1, 4, 7, 6]
    #a = a[::-1]
    print a
    #print partition1(a)
    #print partition2(a)
    print partition3(a)

    with open("Quicksort.txt") as f:
        lines = f.readlines()
    arr = [int(l.rstrip()) for l in lines]
    print len(arr)
    print "Ncomp(estimated)=", int(1.386 * len(arr)*math.log(len(arr)))

    # Q1
    ncmp = 0
    sorteda1 = qsort(arr)
    assert(sorteda1 == list(xrange(1, len(arr)+1)))
    print "Ncomp= ", ncmp

