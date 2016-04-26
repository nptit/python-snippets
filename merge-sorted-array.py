def merge_sorted(l1, l2):
    ''' merge two sorted arrays, simple code, O(n^2)'''
    res = []
    while l1 and l2:
        if l1[0] <= l2[0]:
            res.append(l1.pop(0))
        else:
            res.append(l2.pop(0))

    return res+l1+l2

def merge_sorted(l1, l2):
    '''merge two sorted array l1 and l2 into l1, O(n)'''
    n1, n2 = len(l1), len(l2)
    l1[n1:n1+n2] = [0]*n2

    i = (n1+n2) - 1
    j = n1 - 1
    k = n2 - 1
    while j >= 0 and k >=0:
        if l1[j] >= l2[k]:
            l1[i] = l1[j]
            j -= 1
        else:
            l1[i] = l2[k]
            k -= 1
        i -= 1

    if k >= 0:
        l1[:k+1] = l2[:k+1]

    return l1

def merge_sorted(l1, l2):
    '''merge two sorted array l1 and l2 into l1, O(n)'''
    n1, n2 = len(l1), len(l2)
    res = []

    i, j, k = 0, 0, 0
    while j < n1 and k < n2:
        if l1[j] <= l2[k]:
            res.append(l1[j])
            j += 1
        else:
            res.append(l2[k])
            k += 1

    return res + l1[j:n1] + l2[k:n2]


l1, l2= [1,3,4,6], [1,2,3,8]
print merge_sorted(l1, l2)

print merge_sorted([1,2,3], [4,5,6])
print merge_sorted([1,2,3], [2,4,6])
print merge_sorted([4,5,6], [1,2,3])



