
from math import sqrt
def squareRoot(n):
    if n < 0:
        raise ValueError('input value is negative')
    return sqrt(n)

def squareRoot(n):
    ''' bisect method '''
    if n < 0:
        raise ValueError('input value is negative')

    accuracy = 1.0e-8

    lo = 0
    hi = n + 1.0
    mid = lo + (hi - lo) / 2.0
    while abs(mid*mid - n) > accuracy:
        if mid*mid - n > 0:
            hi = mid
        else:
            lo = mid
        mid = lo + (hi - lo) / 2.0
    return mid


def squareRoot(n):
    ''' newton method: x_n+1 = x_n - f/f' '''
    if n < 0:
        raise ValueError('input value is negative')

    accuracy = 1.e-8
    x = n/2.0
    while abs(x*x - n) > accuracy:
        x = 0.5 * (x + n / x)
    return x



print squareRoot(100)

