__author__ = 'qxu'

def divisors(n):
    # return all divisors of n
    return [d for d in xrange(2L, abs(n)//2+1) if n % d == 0]

def isprime(n):
    return all(n%d!=0 for d in xrange(2L, abs(n)))

def primefactors(n):
    div=divisors(n)
    if isprime(n):
        div.append(n)
    return [i for i in div if isprime(i)]

def primes(n):
    #return list of primers less or equal to n
    return [i for i in xrange(2L,n+1) if isprime(i)]

import math
def isPP1(n):
    # given an integer n, check whether it is a perfect power
    # return the pair if true, else return false
    n=long(n)
    k=long(math.log(n, 2))
    plst=primes(k)
    div=divisors(n)
    print div
    for i in div:
        for p in plst:
            if n == i**p:
                return [i, p]
    return None

def isPP(n):
    # implements the perfect power test by Martin Dietzfelbinger (algorithm 2.3.5)
    # divide and conquer, complexity (log(n))**3
    b = 2
    while 2**b <= n:
        a = 1
        c = n
        while c-a >= 2:
            m = (a+c)//2
            p = min(m**b, n+1)
            if p == n:
                return [m, b]
            elif p < n:
                a = m
            else:
                c = m
        b += 1
    return None

print isPP(78502725751)
print isPP(9)
print isPP(8)
