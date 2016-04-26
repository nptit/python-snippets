
def ndigits(n):
    if n < 0:
        n = -n
    if n == 0:
        return 0
    return 1 + ndigits(n // 10)


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1

    if exp % 2 == 0:
        return recurPower(base**2, exp / 2)
    else:
        return base * recurPower(base, exp - 1)


def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    minab = min(a,b)
    for i in range(b, 0, -1):
        if a % i ==0 and b % i == 0:
            return i


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.

    If b = 0, then the answer is a
    Otherwise, gcd(a, b) is the same as gcd(b, a % b)
    '''
    # Your code here
    if b == 0:
        return a
    return gcdRecur(b, a % b)

#print gcdRecur(10,3)


def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    i = 0
    for c in aStr:
        i += 1
    return i


def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    if aStr:
        return 1 + lenRecur(aStr[1:])
    else:
        return 0






def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string, aStr will be a string that is in alphabetical order

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    nc = len(aStr)
    lb = 0
    ub = nc
    middle = (ub + lb + 1) // 2

    if nc <= 1:
        return char == aStr

    if char == aStr[middle]:
        return True
    elif char < aStr[middle]:
        return isIn(char, aStr[lb:middle])
    else:
        return isIn(char, aStr[middle:ub])


def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def f(x):
    import math
    return 400*math.e**(math.log(0.5)/3.66 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...

    ndiv = int((stop - start) / step)
    values = [ step * f(start + step * i) for i in range(ndiv)]
    return sum(values)


print radiationExposure(0, 4, 0.25)












