def checkio(n, m):
    m, n = max(m, n), min(m, n)
    bm = '{0:b}'.format(m)
    bn = '{0:0{1}b}'.format(n, len(bm))
    return len([1 for i, j in zip(bm, bn) if i != j])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    print checkio(117, 17)
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
