def genPrimes():
    x = 1
    while True:
        x += 1
        if isPrime(x):
            yield x

def isPrime(x):
    if x == 1:
        return False
    return False if any(x % i == 0 for i in range(2, x // 2 + 1)) else True

g = getPrimes()
print g.next()
print g.next()
print g.next()



# Note that our solution makes use of the for/else clause, which
# you can read more about here:
# http://docs.python.org/release/1.5/tut/node23.html

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
