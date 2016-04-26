
def isUniqueChars(s):
    '''check a string has all unique characters, O(n)'''
    return len(set(s)) == len(s)

def isUniqueChars(s):
    '''check a string has all unique characters, no additional data structure allowed, O(n^2)'''
    for i, c in enumerate(s):
        if c in s[:i] or c in c in s[i+1:]:
            return False
    return True

def reverse(s):
    '''reverse a null-terminated string'''
    return s[::-1]

def reverse(s):
    '''reverse a null-terminated string'''
    s = list(s)
    i = 0
    n = len(s)
    while i < n // 2:
        s[i], s[n-i-1] = s[n-i-1], s[i]
        i += 1
    return ''.join(s)

def isPermutations(s1, s2):
    '''given two strings, check whether s1 and s2 are permutation of one another'''
    from collections import Counter
    return Counter(s1) == Counter(s2)

def isPermutations(s1, s2):
    '''given two strings, check whether s1 and s2 are permutation of one another'''
    return sorted(s1) == sorted(s2)

def replaceSpaces(s):
    '''given a string, write a method that replaces all spaces into %20 in place'''
    return s.replace(' ', '%20')

def replaceSpaces(s):
    '''given a string, write a method that replaces all spaces into %20 in place'''
    n = len(s)
    s = list(s)
    for i in range(n-1, -1, -1):
        if s[i] == ' ':
            s[i] = '%20'
    return ''.join(s)

def replaceSpaces(s):
    '''given a string, write a method that replaces all spaces into %20 in place'''
    return ''.join('%20' if c == ' ' else c for c in s)

def runLengthCompression(s):
    '''compress a string by run length'''
    from collections import OrderedDict
    d = OrderedDict()
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    news = ''.join(['{}{}'.format(c, v) for c, v in d.items()])
    return news if len(news) < len(s) else s

if __name__ == '__main__':
    assert isUniqueChars('') == True
    assert isUniqueChars('a') == True
    assert isUniqueChars('aa') == False
    assert isUniqueChars('aba') == False

    assert reverse('') == ''
    assert reverse('a') == 'a'
    assert reverse('aa') == 'aa'
    assert reverse('abc') == 'cba'
    assert reverse('abcd') == 'dcba'

    assert isPermutations('', '') == True
    assert isPermutations('ab', 'ba') == True
    assert isPermutations('aab', 'abb') == False

    assert replaceSpaces('') == ''
    assert replaceSpaces(' ') == '%20'
    assert replaceSpaces('a ') == 'a%20'


    assert runLengthCompression('') == ''
    assert runLengthCompression('abc') == 'abc'
    assert runLengthCompression('aaa') == 'a3'
    assert runLengthCompression('abbbbbz') == 'a1b5z1'
