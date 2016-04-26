def checkio(numbers):
    'relationship bsum(k) = max( bsum(k-2) + l[k], bsum(k-1) + l[k])'
    l = [0] + numbers + [0]
    if len(l) == 3:
        return max(l)

    bsum = [0] * len(l)
    bsum[1] = l[1]
    for i in range(2, len(l)):
        bsum[i] = max(bsum[i-2] + l[i], bsum[i-1] + l[i])
    return bsum[-1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print checkio([-21]) == 0, '1 step'
    print checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27]) #== 125, 'Third'
    print checkio([5, -3, -1, 2]) == 6, 'Fifth'
    assert checkio([5, 6, -10, -7, 4]) == 8, 'First'
    assert checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]) == 393, 'Second'

    print('All ok')
