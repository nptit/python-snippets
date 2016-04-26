
def quickSort(li):
    if len(li) <= 1:
        return li
    else:
        p = li[0]
        lt = [e for e in li[1:] if e < p]
        ge = [e for e in li[1:] if e >= p]
        return quickSort(lt) + [p] + quickSort(ge)

#print quickSort([5, 1, 2, 1, 4])

def partition(li, start, end):
    '''given a list, for pivot = li[0], partition it such that every element to the left is less than pivot,
    and every element on the right >=pivot, do it in place'''
    m = start
    for i in range(m+1, end+1):
        if li[i] < li[start]:
            m += 1
            li[i], li[m] = li[m], li[i]
    li[start], li[m] = li[m], li[start]
    return m

def qSort(li, start, end):
    if start < end:
        pivotPosition = partition(li, start, end)
        qSort(li, start, pivotPosition-1)
        qSort(li, pivotPosition+1, end)


def partition(li, start, end):
    '''given a list, for pivot = li[0], partition it such that every element to the left is less than pivot,
    and every element on the right >=pivot, do it in place'''
    l = start
    r = end

    for i in range(m+1, end+1):
        if li[i] < li[start]:
            m += 1
            li[i], li[m] = li[m], li[i]
    li[start], li[m] = li[m], li[start]
    return m

def qSort(li, start, end):
    if start < end:
        pivotPosition = partition(li, start, end)
        qSort(li, start, pivotPosition-1)
        qSort(li, pivotPosition+1, end)


l = [7, 6, 1, 8, 2,3,9,4,5]
print qSort(l, 0, len(l)-1), l
