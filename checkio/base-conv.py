def numberToBase(n, b):
    # convert positive int n to arbitary base b
    sign = 1
    if n == 0:
        return [0]
    elif n < 0:
        n = -1 * n
        sign = -1

    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return digits[::-1], sign

print numberToBase(4,2)
