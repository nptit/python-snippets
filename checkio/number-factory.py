def factor(n, p):
    # given n and a factor p, find maximum m such that n % p**m
    i = 0
    while n % p**i == 0:
        i += 1
    return i - 1

def checkio(n):
    factors = range(9, 1, -1)

    powers = []
    for f in factors:
        p = factor(n, f)
        n = n / f**p
        powers.append(p)

    return 0 if n != 1 else int(''.join([str(i)*p for i, p in reversed(zip(factors, powers))]))
