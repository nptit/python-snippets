def checkio(n):
    one = sum([True])
    two = sum([True, True])
    i = two
    while i < n:
        new = i
        while True:
            if n == new:
                return False
            if new > n:
                break
            new += i
        i += one
    return True

