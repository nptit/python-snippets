__author__ = 'qxu'


import itertools
def permutations(string):
    return [''.join(t) for t in set(itertools.permutations(string))]

#print permutations('aabb')

def ListPermutations(s):
    '''permutate string'''
    def recursivePermutate(sofar, rest):
        if not rest:
            print sofar
        for i in range(len(rest)):
            nextv = sofar + rest[i]
            remaining = rest[:i] + rest[i+1:]
            recursivePermutate(nextv, remaining)
    recursivePermutate('', s)

#ListPermutations('abc')

def ListPermutations(s):
    '''permutate string'''
    def recursivePermutate(sofar, rest, results=[]):
        if not rest:
            results.append(sofar)
        else:
            for i in range(len(rest)):
                nextv = sofar + rest[i]
                remaining = rest[:i] + rest[i+1:]
                recursivePermutate(nextv, remaining, results)
        return results
    return recursivePermutate('', s)

def ListPermutations(s):
    '''permutate string, needs to handle duplicated letters'''
    def recursivePermutate(sofar, rest, results=[]):
        if not rest:
            results.append(sofar)
        else:
            for i in range(len(rest)):
                nextv = sofar + rest[i]
                remaining = rest[:i] + rest[i+1:]
                recursivePermutate(nextv, remaining, results)
        return results
    return set(recursivePermutate('', s))

def ListPermutations(s):
    '''permutate string, needs to handle duplicated letters'''
    def recursivePermutate(sofar, rest, results=[]):
        if not rest:
            if sofar not in results:
                results.append(sofar)
        else:
            for i in range(len(rest)):
                nextv = sofar + rest[i]
                remaining = rest[:i] + rest[i+1:]
                recursivePermutate(nextv, remaining, results)
        return results
    return recursivePermutate('', s)



def ListSubset(s):
    '''subset string'''
    def recursiveSubset(sofar, rest, results=[]):
        if not rest:
            if sofar not in results:
                results.append(sofar)
        else:
            recursiveSubset(sofar + rest[0], rest[1:], results)
            recursiveSubset(sofar, rest[1:], results)
        return results
    return recursiveSubset('', s)

print ListPermutations('aac')
print ListSubset('aac')

def recursivePermutate(sofar, rest):
    if not rest:
        yield sofar
    else:
        for i in range(len(rest)):
            for perm in recursivePermutate(sofar + rest[i], rest[:i] + rest[i+1:]):
                yield perm


def getPermutations(string, prefix=""):
    if len(string) == 1:
        yield prefix + string
    else:
        for i in xrange(len(string)):
            for perm in getPermutations(string[:i] + string[i+1:], prefix+string[i]):
                yield perm

def getPermutations(string):
    if len(string) == 1:
        yield string
    else:
        for i in xrange(len(string)):
            for perm in getPermutations(string[:i] + string[i+1:]):
                yield string[i] + perm

print list(getPermutations('abc')) == list(recursivePermutate('', 'abc'))


def canMakeSum(li, target, sofar=[]):
    if not li:
        if sum(sofar) == target:
            print sofar
    else:
        canMakeSum(li[1:], target, sofar+[li[0]])
        canMakeSum(li[1:], target, sofar)

canMakeSum([1, 2, 3, 4,5, 6, 7, 8], 7)


def subList(li, sofar=[]):
    if not li:
        yield sofar
    else:
        for sub in subList(li[1:], sofar+[li[0]]):
            yield sub
        for sub in subList(li[1:], sofar):
            yield sub

print list(subList([1,2,3]))
