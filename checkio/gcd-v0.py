def greatest_common_divisor(*args):
    """
        Find the greatest common divisor
    """
    return 1

def gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, a - b)

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def greatest_common_divisor(*args):
    if len(args) == 2:
        return gcd(args[0], args[1])
    return greatest_common_divisor(gcd(args[0], args[1]), args[2:])


print gcd(2,0)
print greatest_common_divisor(10, 5)

exit()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"
