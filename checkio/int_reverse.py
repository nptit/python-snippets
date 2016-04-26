def int_reverse(n):
    'reverse an integer'
    return int(str(n)[::-1])

print int_reverse(102)


def int_reverse(n):
    'reverse an integer'
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n / 10
    nd = len(digits)
    return sum([digits[i] * 10**(nd - i - 1) for i in range(nd)])

def int_reverse(n):
    'reverse an integer'
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n = n / 10
    return r


print int_reverse(100)
