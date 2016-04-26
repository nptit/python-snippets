
def merge2(l1, l2):
    n1, n2 = len(l1), len(l2)
    i, j = 0, 0
    res = []
    while i < n1 and j < n2:
        if l1[i] <= l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1

    return res+l1[i:]+l2[j:]

l1 = [1,2,3,4]
l2 = [1, 5, 6]
print merge2(l1, l2)

def mergeK(ll):
    '''ll: list of sorted lists'''
    k = len(ll)
    if k <= 1:
        return ll[0]
    elif k == 2:
        return merge2(ll[0], ll[1])

    return merge2(mergeK(ll[0:k//2]), mergeK(ll[k//2:]))


l1 = [1,2, 8]
l2 = [1, 2, 3]
l3 = [1, 4]

print mergeK([l1, l2, l3])

A1 = [1, 5, 8, 9 ]
A2 = [ 2, 3, 7, 10 ]
A3 = [ 4, 6, 11, 15 ]
A4 = [ 9, 14, 16, 19 ]
A5 = [ 2, 4, 6, 9 ]

print mergeK([A1, A2, A3, A4, A5]) == [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9, 9, 10, 11, 14, 15, 16, 19]


def mergesort(l):
    n = len(l)
    if n <= 1:
        return l
    elif n == 2:
        return [min(l[0], l[1]), max(l[0], l[1])]

    mid = n // 2
    return merge2(mergesort(l[0:mid]), mergesort(l[mid:]))

print mergesort([2,3,1,1])

def selectionSort(l):
    for i, v in enumerate(l[:-1]):
        min_idx, min_rest = min(enumerate(l[i+1:], i+1), key=lambda x: x[1])

        if min_rest <= v:
            l[i], l[min_idx] = l[min_idx], l[i]

    return l


print selectionSort([3, 2, 1, 1, 0, 5])
print selectionSort([1,2])


def bubbleSort(l):
    n = len(l)
    for i in range(n-1, -1, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

print bubbleSort([1,3,2,5,1])
