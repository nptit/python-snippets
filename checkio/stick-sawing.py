def checkio(length):
    'brute-force method'
    'given an integer, divide it into sum of longest series of triangular numbers'
    'length == sum [x*(x+1)/2, ..., (x+p-1)*(x+p)/2], solve for p and x'
    for p in range(20, 0, -1):
        for x in range(1, 20):
            target = sum([y * (y + 1) for y in range(x, x + p)]) / 2
            if target == length:
                return [i * (i + 1) / 2 for i in range(x, x + p)]
    return []

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
