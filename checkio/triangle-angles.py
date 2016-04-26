import math


def checkio(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return [0, 0, 0]
    if a == b == c:
        return [60, 60, 60]

    alpha = math.acos((b*b + c*c - a*a)/(2.0*b*c))/math.pi
    beta = math.acos((a*a + c*c - b*b)/(2.0*a*c))/math.pi
    gamma = math.acos((a*a + b*b - c*c)/(2.0*a*b))/math.pi
    return [int(round(a*180)) for a in sorted([alpha, beta, gamma])]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
