import string

def checkio(number):
    alphabeta = string.digits + string.letters[-26:]
    start = max([alphabeta.index(c) for c in number]) + 1
    for k in range(start, 37):
        if int(number, k) % ( k - 1) == 0:
            return k
    return 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"18") == 10, "Simple decimal"
    assert checkio(u"1010101011") == 2, "Any number is divisible by 1"
    assert checkio(u"222") == 3, "3rd test"
    assert checkio(u"A23B") == 14, "It's not a hex"
    assert checkio(u"IDDQD") == 0, "k is not exist"
    print('Local tests done')
