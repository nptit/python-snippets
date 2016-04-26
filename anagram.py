


def anagram(s1, s2):
    '''check whether two strings are anagrams, ignore space and capitalization'''
    import string, collections
    s1 = [c.lower() for c in s1 if c in string.letters]
    s2 = [c.lower() for c in s2 if c in string.letters]
    return collections.Counter(s1) == collections.Counter(s2)

def anagram(s1, s2):
    '''check whether two strings are anagrams, ignore space and capitalization'''
    import string, collections
    s1 = [c.lower() for c in s1 if c in string.letters]
    s2 = [c.lower() for c in s2 if c in string.letters]
    return sorted(s1) == sorted(s2)

def anagram(s1, s2):
    '''check whether two strings are anagrams, ignore space and capitalization'''
    import string
    s1 = [c.lower() for c in s1 if c in string.letters]
    s2 = [c.lower() for c in s2 if c in string.letters]

    count = {}
    for c in s1:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    for c in s2:
        if c in count:
            count[c] -= 1
        else:
            return False

    for c in count:
        if count[c] != 0:
            return False

    return True


assert anagram('o d g', 'god') == True
assert anagram('clint eastwood', 'old west action') == True

def pair_sum(alist, k):
    ''' given an integer array, out all the unique pairs that sum up to a specific value k'''
    result = set()
    for el in alist:
        diff = k - el
        if diff in alist:
            result.add((min(el, diff), max(el, diff)))
    return len(result)

def pair_sum(alist, k):
    ''' given an integer array, out all the unique pairs that sum up to a specific value k'''
    result = []
    for el in set(alist):
        diff = k - el
        if diff in alist and el <= diff:
            result.append((el, diff))
    return len(result)

def pair_sum(alist, k):
    ''' given an integer array, out all the unique pairs that sum up to a specific value k'''
    if len(alist) < 2:
        return

    seen = set()
    result = set()
    for el in alist:
        diff = k - el
        if diff not in seen:
            seen.add(el)
        else:
            result.add((min(el, diff), max(el, diff)))

    return len(result)

assert pair_sum([1,3,2,2], 4) == 2
assert pair_sum([1, 2, 3, 1], 3) == 1
assert pair_sum([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10) == 6



def powerof2(n):
    ''' given an integer n, check whether it is power of two'''
    if n < 0:
        return False
    elif n == 1:
        return True

    d, r = divmod(n, 2)
    if r != 0:
        return False

    return powerof2(d)


assert powerof2(5) == False
assert powerof2(2**15) == True
assert powerof2(2**15-1) == False


def finder(arr1, arr2):
    ''' arr1 is an array of non-negative integers, arr2 is arr1 with a random element deleted, find that number'''
    return sum(arr1) - sum(arr2)

def finder(arr1, arr2):
    return reduce(lambda a, b: a^b, arr1+arr2, 0)

def finder(arr1, arr2):
    from collections import Counter
    diffcounter = Counter(arr1) - Counter(arr2)
    return diffcounter.keys()[0]

assert finder(range(1, 8), [3,7,2,1,4,6]) == 5


def largest_cont_sum(arr):
    '''given an array of positive and negative numbers, find largest continous sum-- brute force'''
    maxsum, indi, indj = arr[0], 0, 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sumij = sum(arr[i:j+1])
            if sumij > maxsum:
                indi, indj = i, j
                maxsum = sumij
    return (indi, indj, maxsum)

assert largest_cont_sum([1,2,-1, 3,4, 10, 10, -10, -1]) == (0, 6, 29)


def largest_cont_sum(arr):
    maxarr = [0 for _ in arr]
    maxsofar = 0
    for i in range(len(arr)):
        s = maxsofar + arr[i]
        if s < 0:
            maxsofar = 0
            maxarr[i] = maxsofar
        else:
            maxarr[i] = s
            maxsofar = s

def largest_cont_sum(arr):
    maxsofar = 0
    best = 0
    for i in range(len(arr)):
        s = maxsofar + arr[i]
        maxsofar = 0 if s < 0 else s
        if maxsofar > best:
            best = maxsofar

    return best

def largest_cont_sum(arr):
    if len(arr) < 1:
        return 0

    current_sum = best = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        best = max(current_sum, best)

    return best

assert largest_cont_sum([1,2,-1, 3,4, 10, 10, -10, -1]) == 29
assert largest_cont_sum([1,-1]) == 1


def rev_word(s):
    '''given a string, reverse the sequence of words in it. remove leading and tailing spaces'''
    words = s.split(' ')
    return ' '.join(w for w in words[::-1] if w)

def rev_word(s):
    '''given a string, reverse the sequence of words in it. remove leading and tailing spaces'''
    s = s.rstrip().lstrip()
    words = []

    start = 0
    end = 0
    for i, c in enumerate(s):
        if c == ' ':
            end = i - 1
            words.append(s[start:end+1])
            start = i+1

    words.append(s[start:])
    res = ''
    while words:
        res += words.pop()
        res += ' '

    return res.strip()

def rev_word(s):
    '''given a string, reverse the sequence of words in it. remove leading and tailing spaces'''
    s = s.rstrip().lstrip()
    words = []

    start = 0
    end = 0
    for i, c in enumerate(s):
        if c == ' ':
            end = i - 1
            words.append(s[start:end+1])
            start = i+1

    words.append(s[start:])
    return ' '.join(reversed(words))


def rev_word(s):
    '''given a string, reverse the sequence of words in it. remove leading and tailing spaces'''
    words = []

    i = 0
    while i < len(s):
        if s[i] != ' ':
            start = i
            while i < len(s) and s[i] != ' ':
                i += 1
            words.append(s[start:i])
        i += 1

    return ' '.join(reversed(words))

#print rev_word('    space before')
#print rev_word('Hi John,   are you ready to go?')

def compress(s):
    '''given a string in the form AAAAABBBBCCC, compress it to A5B4C3--run length compression algorithm'''
    lens = len(s)

    i = 0
    res = ''
    while i < lens:
        i += 1
        count = 1
        while i < lens and s[i] == s[i-1]:
            count += 1
            i += 1
        res += s[i-1] + str(count)
    return res

assert compress('A') == 'A1'
assert compress('AAABB') == 'A3B2'


def uni_char(s):
    '''check a string consist of all unique characters, return True, else False'''
    return len(set(s)) == len(s)

def uni_char(s):
    '''check a string consist of all unique characters, return True, else False'''
    d = {}
    for c in s:
        if c in d:
            return False
        else:
            d[c] = 1

    return True

assert uni_char('abcd') == True
assert uni_char('aab') == False









