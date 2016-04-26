
from collections import Counter, OrderedDict
def anagram(s, t):
    return Counter(s) == Counter(t)

def anagrams(array):
    '''Given an array of strings, return all groups of strings that are anagrams.

    Example
    Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].

    Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].
    Note
    All inputs will be in lower-case'''
    d = OrderedDict()
    for s in array:
        for key in d:
            if anagram(s, key):
                d[key].append(s)
                break
        else:
            d[s] = [s]

    results = []
    for key in d:
        if len(d[key]) > 1:
            results.extend(d[key])
    return results

def anagrams(array):
    maps = OrderedDict()
    for s in array:
        sorts = ''.join(sorted(s))
        if sorts in maps:
            maps[sorts].append(s)
        else:
            maps[sorts] = [s]

    results = []
    for key in maps:
        if len(maps[key]) > 1:
            results.extend(maps[key])
    return results

print anagrams(["ab", "ba", "cd", "dc", "e"])
print anagrams(["lint", "intl", "inlt", "code"])
print anagrams([])
print anagrams(['a','b'])
