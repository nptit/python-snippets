__author__ = 'qxu'


class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci2(self, n):
        # write your code here
        if n==1 or n==2:
            return n-1
        return self.fibonacci(n-1)+self.fibonacci(n-2)

    def fibonacci(self, n):
        # write your code here
        f1,f2=0,1
        for i in xrange(n):
            f1,f2=f1+f2,f1
        return f2

#s=Solution()
#print s.fibonacci(5)



class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        #if n==1:
        #    return 1
        #elif n==2:
        #    return 2
        #return self.climbStairs(n-1)+self.climbStairs(n-2)
        a,b=1,2
        for i in xrange(n-1):
            a,b=b,a+b
        return a




def fib_v0(n):
    if n < 2:
        return n
    else:
        return fib_v0(n-1) + fib_v0(n-2)


def fib(n):
    def additiveSequence(n, f0, f1):
        if n == 0:
            return f0
        elif n == 1:
            return f1
        return additiveSequence(n-1, f1, f0+f1)

    return additiveSequence(n, 0, 1)


def isPalindrome(s):
    return s==s[::-1]

def isPalindrome(s):
    if len(s) <=1:
        return True
    else:
        return s[0]==s[-1] and isPalindrome(s[1:-1])


def isPalindrome(s):
    def _isPalindrome(s, p1, p2):
        if p1 >= p2:
            return True
        else:
            return s[p1] == s[p2] and _isPalindrome(s, p1+1, p2-1)
    return _isPalindrome(s, 0, len(s)-1)

#print isPalindrome('ab')


def digits(n, results=None):
    if not results:
        results = []

    if n < 10:
        results.append(n)
        return results
    else:
        d, r = divmod(n, 10)
        results.append(r)
        return digits(d, results)

print digits(10012899)

def digitsSum(n):
    if n == 0:
        return n
    else:
        return digitsSum(n//10) + n % 10

print digitsSum(10012899)

def digitsRoot(n):
    if n < 10:
        return n
    else:
        return digitsRoot(digitsSum(n))

def digitsRoot_v2(n):
    ''' digital root of n = 1 + ( (n - 1) % 9 )'''
    return 1 + (n-1) % 9

print digitsRoot(90009) == digitsRoot_v2(90009)



def digitsRoot(n):
    if n < 10:
        return n
    else:
        n = digitsRoot(n // 10) + n % 10
        return digitsRoot(n)

print digitsRoot(901009) == digitsRoot_v2(901009)
