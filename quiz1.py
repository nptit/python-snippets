def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x


def isPalindrome(aString):
    '''
    aString: a string
    '''
    # Your code here
    n = len(aString)
    return all(aString[i] == aString[n -i -1] for i in range(n))

#print isPalindrome('')
#print isPalindrome('ab')


def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    return sum(i*j for i,j in zip(listA, listB))

#print dotProduct([1,2,3], [1,0,0])

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    result = []
    for el in aList:
        if isinstance(el, (list, tuple)):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result


#print flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])


def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    common_keys = set()
    diff_keys1 = set()
    diff_keys2 = set()
    for k1 in d1:
        if k1 in d2:
            common_keys.add(k1)
        else:
            diff_keys1.add(k1)

    for k2 in d2:
        if k2 not in d1:
            diff_keys2.add(k2)

    inter = {}
    diff = {}

    for k in common_keys:
        inter[k] = f(d1[k], d2[k])

    for k in diff_keys1:
        diff[k]= d1[k]

    for k in diff_keys2:
        diff[k]= d2[k]


    return (inter, diff)

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    common_keys = set(d1.keys()) & set(d2.keys())
    inter = dict((k, f(d1[k], d2[k])) for k in common_keys)

    diff1 = dict((k, d1[k]) for k in d1 if k not in common_keys)
    diff2 = dict((k, d2[k]) for k in d2 if k not in common_keys)
    diff1.update(diff2)

    return (inter, diff1)


# d1 = {1:30, 2:20, 3:30, 5:80}
# d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

# def f(a, b):
#     return a>b

# print dict_interdiff({1: 2}, {2: 1})


def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    indices = []
    for i in range(len(L)):
        if not f(L[i]):
            indices.append(i)

    for i in indices[::-1]:
        L.pop(i)

    return len(L)
    #return sum(f(el) for el in L)


def f(s):
    return 'a' in s

L = ['a', 'b', 'a']
print satisfiesF(L)
print L

#run_satisfiesF(L, satisfiesF)

