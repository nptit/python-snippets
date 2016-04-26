import string


def checkio(str_number, radix):
    table = string.digits + string.letters[26:]
    ndec = 0

    for i, d in enumerate(str_number[::-1]):
        n = table.index(d)
        if n >= radix:
            return -1
        ndec += n * radix**i
    return ndec

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"AF", 16) == 175, "Hex"
    assert checkio(u"101", 2) == 5, "Bin"
    assert checkio(u"101", 5) == 26, "5 base"
    assert checkio(u"Z", 36) == 35, "Z base"
    assert checkio(u"AB", 10) == -1, "B > A > 10"
