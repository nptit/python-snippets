def merge(l1, l2):
    stack1 = l1[:]
    stack2 = l2[:]
    res = []
    while stack1 and stack2:
        if stack1[0] <= stack2[0]:
            res.append(stack1.pop(0))
        else:
            res.append(stack2.pop(0))

    return res+stack1+stack2

def merge(l1, l2):
    stack1 = l1[:]
    stack2 = l2[:]
    res = []
    while stack1 and stack2:
        if stack1[0] <= stack2[0]:
            res.append(stack1.pop(0))
        else:
            res.append(stack2.pop(0))

    if stack1:
        res += stack1
    if stack2:
        res += stack2
    return res


def merge(l1, l2):
    n1, n2 = len(l1), len(l2)
    n12 = n1 + n2
    l1[n1:n12] = [0]*n2
    i, j = n1-1, n2-1
    k = n1+n2-1
    while i >= 0 and j >= 0:
        if l1[i] <= l2[j]:
            l1[k] = l2[j]
            j -= 1
        else:
            l1[k] = l1[i]
            i -= 1
        k -= 1

    if j > 0:
        l1[:j+1] = l2[:j+1]

    return l1


print merge([1,2,3], [])
print merge([1,2,5, 6], [1, 1,2,3])


def reverseString(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1]+reverseString(s[:-1])

def reverseString(s):
    n = len(s)
    s = list(s)
    for i in range(n//2):
        s[i], s[n-1-i] = s[n-1-i], s[i]
    return ''.join(s)

print reverseString('abc4')

def top2(l):
    max1 = -float('Inf')
    max2 = -float('Inf')
    for i in range(len(l)):
        if l[i] > max1:
            max2 = max1
            max1 = l[i]
        elif l[i] > max2:
            max2 = l[i]
    return (max1,max2)

print top2([1,2,3,4])
