


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


class Stack(object):

    def __init__(self, items=[]):
        self.__data = items

    def pop(self):
        return self.__data.pop()

    def peek(self):
        return self.__data[-1] if self.__data else None

    def len(self):
        return len(self.__data)

    def push(self, item):
        self.__data.append(item)

    def isempty(self):
        return True if len(self.__data) == 0 else False

    def __repr__(self):
        return str(self.__data)

# stack = Stack([1,2,3])
# stack.push(4)
# print stack
# print stack.isempty()
# print stack.peek(), stack.pop()
# print stack.peek()

def balance_check(s):
    ''' given a string of openning and closing parentheses, check whether it is balanced, return True or False'''
    pairs = {'{': '}', '(':')', '[':']'}
    stack = Stack()
    for c in s:
        if c in pairs:
            stack.push(c)
        else:
            if pairs[stack.peek()] == c:
                stack.pop()
            else:
                return False

    return not stack.isempty()

assert balance_check('([)]') == False
assert balance_check('[](){([[[]]])}') == True
assert balance_check('') == True


class Queue2Stacks(object):
    ''' implement a queue using two stacks'''
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack2.append(element)

    def dequeue(self):
        if not self.stack1:
            if not self.stack2:
                return None
            else:
                while self.stack2:
                    self.stack1.append(self.stack2.pop())
        return self.stack1.pop()

    def __repr__(self):
        return "stack1= {}, stack2= {}".format(self.stack1, self.stack2)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None

    def __repr__(self):
        return str(self.value)



class LinkedList(object):
    def __init__(self):
        self.headnode = None

    def addnode(self, newnode):
        if not self.headnode:
            self.headnode = newnode
        else:
            node = self.headnode
            while node.nextnode:
                node = node.nextnode
            node.nextnode = newnode

a = Node(1)
b = Node(2)
c = Node(3)

x = LinkedList()
x.addnode(a)
x.addnode(b)
x.addnode(c)

def cycle_check_in_SingleLinkedList(head):
    '''check existence of a cycle in a single linked list, rabbit turtle algorithms '''
    m1 = head
    m2 = head
    while m1.nextnode != None and m2.nextnode != None:
        m1 = m1.nextnode
        m2 = m2.nextnode.nextnode
        if m1 == m2:
            return True
    return False

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.nextnode=b
b.nextnode=c
c.nextnode=d
d.nextnode=b

assert cycle_check_in_SingleLinkedList(a) == True

def reverseLinkedList(head):
    '''reverse a single linked list in place'''
    node = head
    nodes = [head]
    while node.nextnode != None:
        node = node.nextnode
        nodes.append(node)

    n = len(nodes)
    nodes[0].nextnode = None
    for i in range(1, n):
        nodes[i].nextnode = nodes[i-1]
    return nodes[-1]

def reverseLinkedList(head):
    '''reverse a single linked list in place'''
    current = head
    previous = None
    nextnode = None
    while current:
        nextnode = current.nextnode
        current.nextnode = previous
        previous = current
        current = nextnode

    return previous

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.nextnode = b
b.nextnode = c
c.nextnode = d

x = reverseLinkedList(a)
assert x == d

def nth2last(n, head):
    '''return the nth node from the last node, 1->2->3->4->5, e.g. n=2 returns 4 '''
    count = 0
    current = head
    while current:
        count += 1
        current = current.nextnode

    k = count - n + 1
    count = 0
    current = head
    while current:
        count += 1
        if count == k:
            return current
        current = current.nextnode

def nth2last(n, head):
    '''return the nth node from the last node, 1->2->3->4->5, e.g. n=2 returns 4, using two pointers '''
    pleft = head
    pright = head
    for i in range(n):
        if not pright.nextnode:
            raise LookupError('Error: n is bigger than list')
        pright = pright.nextnode

    while pright:
        pleft = pleft.nextnode
        pright = pright.nextnode

    return pleft


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

assert nth2last(2, a) == d


def rec_sum(n):
    '''Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer'''
    if n == 0:
        return 0
    return n + rec_sum(n-1)


assert rec_sum(10) == 55
assert rec_sum(2) == 3


def sum_func(n):
    '''Given an integer, create a function which returns the sum of all the individual digits in that integer. For example: if n = 4321, return 4+3+2+1'''
    if n == 0:
        return 0
    n, r = divmod(n, 10)
    return r + sum_func(n)

assert sum_func(4321) == 10


def word_split(phrase, wordlist):
    '''
    Create a function called word_split() which takes in a string phrase and a set
    list_of_words. The function will then determine if it is possible to
    split the string in a way in which words can be
    made from the list of words. You can assume the phrase will
    only contain words found in the dictionary if it is
    completely splittable. word_split('themanran',['the','ran','man'])
    '''
    print "phrase=", phrase
    result = []
    for w in wordlist:
        n = len(w)
        if phrase[:n] == w:
            result.append(w)
            result.extend(word_split(phrase[n:], wordlist))

    return result

def word_split(phrase, wordlist, result = None):
    '''
    Create a function called word_split() which takes in a string phrase and a set
    list_of_words. The function will then determine if it is possible to
    split the string in a way in which words can be
    made from the list of words. You can assume the phrase will
    only contain words found in the dictionary if it is
    completely splittable. word_split('themanran',['the','ran','man'])
    '''
    print "phrase=", phrase
    if not result:
        result = []
    for w in wordlist:
        n = len(w)
        if phrase[:n] == w:
            result.append(w)
            return word_split(phrase[n:], wordlist, result)
    return result

#print word_split('themanran',['the','ran','man'])


def reverse_string(s):
    '''reverse a string using recursion'''
    if len(s) < 2:
        return s
    return reverse_string(s[1:]) + s[0]

assert reverse_string('abc') == 'cba'

def permutate_string(s):
    ''' find all possible permutation of a string '''
    if len(s) <= 1:
        return [s]

    first = s[0]
    rest = s[1:]
    res = []
    for el in permutate_string(rest):
        for i in range(len(el)+1):
            res.append(el[:i] + first + el[i:])

    return res

#print permutate_string('abc')

def fib(n):
    '''return nth number of fibnacci sequence, 0, 1, 1, 2, 3, etc'''
    if n in [0, 1]:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

#print fib(200)

mem = {}
def fib(n):
    if n in mem:
        return mem[n]
    if n in [0, 1]:
        return n
    else:
        f = fib(n-1) + fib(n-2)
        mem[n] = f
        return f

#print fib(200)

from functools import wraps
def memoize(f):
    """ Memoization decorator for a function taking one or more arguments. """
    class memodict(dict):
        def __getitem__(self, *key):
            return dict.__getitem__(self, key)
        def __missing__(self, key):
            ret = self[key] = f(*key)
            return ret
    return memodict().__getitem__

def coinchange_v0(n, changes):
    '''given an amount n, and a list of distint changes, what is the fewest coins that add up to the n?'''
    if n < 0:
        return float('Inf')

    elif n == 0:
        return 0
    else:
        return 1 + min(coinchange_v0(n - c, changes) for c in changes)


mem = {}
def coinchange_mem(n, changes):
    '''given an amount n, and a list of distint changes, what is the fewest coins that add up to the n?'''
    if n in mem:
        return mem[n]

    if n < 0:
        return float('Inf')
    elif n == 0:
        return 0
    else:
        v = 1 + min(coinchange_mem(n - c, changes) for c in changes)
        mem[n] = v
        return v

assert coinchange_mem(21, [1, 2, 5]) == coinchange_v0(21, [1, 2, 5])

def coinchange(n, changes):
    mem = {}
    def coinchange_mem(n, changes):
        '''given an amount n, and a list of distint changes, what is the fewest coins that add up to the n?'''
        if n < 0:
            return float('Inf')
        elif n == 0:
            return 0

        if n not in mem:
            mem[n] = 1 + min(coinchange_mem(n - c, changes) for c in changes)
        return mem[n]
    return coinchange_mem(n, changes)

assert coinchange(22, [1, 2, 7]) == 4


def coinchange_dp(n, changes):
    table = [float('Inf') for _ in range(n+1)]
    table[0] = 0
    for e in range(n+1):
        ds = [e - c for c in changes if e - c >=0]
        if ds:
            table[e] = 1 + min(table[x] for x in ds)

    return table[-1]

assert coinchange_dp(22, [1, 5, 10, 25]) == 4
assert coinchange_dp(6, [5, 10, 25]) == coinchange(6, [5, 10, 25])


def qsort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [el for el in arr[1:] if el <= pivot]
    right = [el for el in arr[1:] if el > pivot]
    return qsort(left) + [pivot] + qsort(right)

assert qsort([1, 3, 5, 2, 1]) == [1, 1, 2,3,5]



def index_product(arr):
    '''given an array, return an array of the same size, at each position,
    the value is the product of the rest of the positions, no division allowed'''
    n = len(arr)
    res = [None for _ in arr]

    leftprod = 1
    i = 0
    while i < n:
        res[i] = leftprod
        leftprod *= arr[i]
        i += 1

    i = n -1
    rightprod = 1
    while i >= 0:
        res[i] *= rightprod
        rightprod *= arr[i]
        i -= 1

    return res

assert index_product([1,2,3]) == [6,3,2]





