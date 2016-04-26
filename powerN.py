
def power(x, n):
    if n == 0:
        return 1

    half = power(x, n//2)
    result = half*half
    return result if n % 2 == 0 else x*result

def power(x, n):
    if n < 0:
        return power(x, -n)
    if n == 0:
        return 1

    product = power(x*x, n//2)
    return product if n % 2 == 0 else x*product




def fastPower(a, b, n):
    '''calculate a^n % b '''
    if b == 0:
        raise ValueError('b cannot be zero')

    if n == 0:
        return 1

    result = fastPower(a, b, n // 2)
    return result*result % b if n%2 == 0 else a*result**2 % b

print power(2,101)
print fastPower(2,3, 2^33)


def fastPower(a, b, n):
    ans = 1
    while n > 0:
        if n % 2 == 1:
            ans = ans * a % b
        a = a * a % b
        n = n / 2
    return ans % b

print fastPower(2,3, 2^33)
