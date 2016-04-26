def checkio(food):
    consumed, m = 0, 0
    while food - consumed >= 0:
        m += 1
        nbirds = m * (m + 1) / 2
        consumed += nbirds

    leftover = food - (consumed - nbirds)
    nbirds = m * (m -1 ) / 2
    return nbirds if leftover <= nbirds else leftover

if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(3) == 2

    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
