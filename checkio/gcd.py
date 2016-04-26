def gcd(a, b):
    'gcd between two numbers'
    while b:
        a, b = b, a%b
    return a

def greatest_common_divisor(*args):
    if len(args) == 2:
        return gcd(args[0], args[1])
    r = list(args[2:])
    r.append(gcd(args[0], args[1]))
    return greatest_common_divisor(*r)

def greatest_common_divisor(*args):
    return reduce(gcd, (args))

# from functools import reduce
# from fractions import gcd
# def greatest_common_divisor(*args):
#     return reduce(gcd,(args))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"
