import math


def polysum(n, s):
    '''given number of sides (n) and edge length (s),
    return the sum of area and perimeter**2 rounded to 4 decimal places'''
    area = n * s * s / math.tan(math.pi / n) / 4.0
    perimeter = n * s
    return round(area + perimeter**2, 4)

if __name__ == '__main__':
    assert polysum(4, 1) == 17
