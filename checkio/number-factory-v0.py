from operator import mul

def fnp(n, p):
    # given n and a prime p, find maximum m such that n % p**m
    i = 0
    while n % p**i == 0:
        i += 1
    return i - 1

def checkio(n):
    primes = [2, 3, 5, 7]
    powers = [fnp(n, p) for p in primes]
    nn = reduce(mul, [i**j for i,j in zip(primes, powers)], 1)

    if nn != n:
        return 0

    sixes, fours = 0, 0
    eights, twos = divmod(powers[0], 3)
    nines, threes = divmod(powers[1], 2)
    fives = powers[2]
    sevens = powers[3]

    if twos >= 1 and threes == 1:
        sixes += 1
        twos -= 1
        threes -= 1
    elif twos >= 2:
        fours += 1
        twos -= 2

    string=''.join(['2'*twos, '3'*threes, '4'*fours, '5'*fives, '6'*sixes, '7'*sevens, '8'*eights, '9'*nines])
    return int(string)

