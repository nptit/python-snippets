def fastpower(x, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        return fastpower(x, n // 2)**2
    else:
        return x*fastpower(x, (n - 1) // 2)**2

def fastpower(x, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        return fastpower(x, n // 2)**2
    else:
        return x*fastpower(x, n -1)

def fastpower(x, n, b):
    'calculate x**n % b'
    if n == 0:
        return 1

    if n % 2 == 0:
        return fastpower(x, n // 2, b)**2 % b
    else:
        return x*fastpower(x, n -1, b) % b


print fastpower(0,222,5)

