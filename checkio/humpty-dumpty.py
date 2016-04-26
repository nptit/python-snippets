from math import pi, sqrt, atanh, asin

def checkio(height, width):
    'see https://en.wikipedia.org/wiki/Spheroid'
    c, a = height / 2.0, width / 2.0
    V = a**2 * c * 4 * pi / 3.0

    if c < a: # olate
        e = sqrt(1 - c**2 / a**2)
        S = 2 * pi * a**2* (1 + (1 - e**2) * atanh(e) / e)
    elif c > a: #problate
        e = sqrt(1 - a**2 / c**2)
        S = 2 * pi * a**2 * (1 + c * asin(e) / (a * e))
    else:
        S = 4 * pi * c**2

    return [round(V, 2), round(S, 2)]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
