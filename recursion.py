
def power(x, n):
    '''
    implement x**n recursively
    :param x: base
    :param n: power
    :return: x**n
    '''

    if n == 0:
       return 1
    if n%2 == 0:
        return power(x*x, n//2)
    else:
        return x*power(x*x, (n-1)//2)

def flatten_list(a, result=None):
    """Flattens a nested list.

        >>> flatten_list([ [1, 2, [3, 4] ], [5, 6], 7])
        [1, 2, 3, 4, 5, 6, 7]
    """
    if result is None:
        result = []

    for x in a:
        if isinstance(x, list):
            flatten_list(x, result)
        else:
            result.append(x)

    return result


def iter_flatten(iterable):
    it = iter(iterable)
    for e in it:
        if isinstance(e, (list, tuple)):
            for f in iter_flatten(e):
                yield f
        else:
            yield e

def flatten(l, ltypes=(list, tuple)):
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return ltype(l)

def flatten_list(l):
    out = []
    for item in l:
        if isinstance(item, (list, tuple)):
            out.extend(flatten_list(item))
        else:
            out.append(item)
    return out

#a = [1, 2, [3, 4], [5, 6, [7, 8, [9, 10]]]]
#print flatten_list(a)
#print list(iter_flatten(a))
#print list(flatten(a))



def flatten_dict(d, result={}, prv_keys = []):
    for k, v in d.iteritems():
        if isinstance(v, dict):
            flatten_dict(v, result, prv_keys + [k])
        else:
            result['.'.join(prv_keys + [k])] = v

    return result


def flatten_dict(d, prefix = '', previous_keys = [], sep = '_'):
    out = {}
    for k, v in d.items():
        if isinstance(v, dict):
            out.update(flatten_dict(v, k + sep, previous_keys + [k]))
        else:
            out.update({sep.join(previous_keys+[k]): v})
    return out

def flatten_dict(d):
    def items():
        for key, value in d.items():
            if isinstance(value, dict):
                for subkey, subvalue in flatten_dict(value).items():
                    yield key + "." + subkey, subvalue
            else:
                yield key, value
    return dict(items())

#print flatten_dict({'a': 1, '3': {'b': {'x': 22, 'y': 3}}, 'c': 4})


"""
Given two strings of lowercase letters, a and b, print the longest string x of lowercase letters such that there is
a permutation of x that is a subsequence of a and there is a permutation of x that is a subsequence of b. If several
x satisfy the criteria above, choose the first one in alphabetical order. Example: given "the" and "street" output "et"
"""

from collections import Counter

def common_permutation(a, b):
    return ''.join(k * v for k, v in sorted((Counter(a) & Counter(b)).items()))

print common_permutation('pretty', 'women')
print common_permutation('walking', 'down')
print common_permutation('the', 'street')
print common_permutation('aaabbbbccdddddd', 'bbdddcccaaaaaaadd')
print common_permutation('bbdddcccaaaaaaadd','aaabbbbccdddddd')
