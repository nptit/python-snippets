from functools import wraps

def memoize(f):
    memo = {}
    @wraps(f)
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fib(n):
    if n in (0, 1):
        return n
    return fib(n-1) + fib(n-2)


print(fib(499))

print fib.__name__
