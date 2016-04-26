def isprime(n):
    #return all(n%i!=0 for i in range(2, n))
    return True if 2**n % n == 2 or n==2 else False

def checkio(n):
    zero = sum([False])
    one = sum([True])
    two = sum([True, True])
    i = two
    while i < n:
        new = i
        while True:
            new += new
            if n == new:
                return False
            if new > n:
                break
        i += one
    return True



print checkio(9999)

