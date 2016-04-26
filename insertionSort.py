def insertionSort(l):
    ''' sort a list by insertion sort'''
    n = len(l)
    for i in range(1, n):
        j = i
        while j > 0 and l[j-1] > l[j]:
            l[j-1], l[j] = l[j], l[j-1]
            j -= 1
    return l


print insertionSort([2, 0.5, 1,2,-1])
