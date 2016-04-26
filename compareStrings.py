
def compareStrings(s, t):
    ''' determine whether string s contain string t, e.g ABCD contains ABC, but not AABC'''
    from collections import Counter
    cs = Counter(s)
    ct = Counter(t)
    return all(cs[key] >= ct[key] for key in ct)

def compareStrings(s, t):
    ''' determine whether string s contain string t, e.g ABCD contains ABC, but not AABC'''
    cs, ct = count(s), count(t)
    for key in ct:
        if key not in cs or cs[key] < ct[key]:
            return False
    return True

def count(s):
    '''given a string s, count each char, and store it into a dict'''
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

if __name__ == '__main__':
    assert compareStrings('ABCD', 'ABC') == True
    assert compareStrings('ABCD', 'AAE') == False
    assert compareStrings('', '') == True
    assert compareStrings('A', '') == True
