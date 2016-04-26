def checkio(opacity):
    fib20 = list(fib(20))
    opacity_list = [10000]
    for i in range(1, 5001):
        if i in fib20:
            opacity_list.append(opacity_list[-1] - i)
        else:
            opacity_list.append(opacity_list[-1] + 1)
    return opacity_list.index(opacity)

def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
