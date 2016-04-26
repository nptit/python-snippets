from math import sqrt


def area_triangle(lol):
    'calculate area of a triangle given three corners using Herons formula, given list of 3 points'
    dxy = lambda p1, p2: sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    p1, p2, p3 = lol
    a, b, c = dxy(p1, p2), dxy(p2, p3), dxy(p1, p3)
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))

def checkio(data):
    'polygon can be divided into sum of triangles, we can use a recursive algorithm'
    'by eliminating one vertex at a time'
    if len(data) == 3:
        return area_triangle(data)
    return area_triangle([data[0], data[1], data[-1]]) + checkio(data[1:])



if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    print area_triangle([[1, 1], [9, 9], [9, 1]])

    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio([[1, 1], [9, 9], [9, 1]]), 32), "The half of the square"
    assert almost_equal(checkio([[4, 10], [7, 1], [1, 4]]), 22.5), "Triangle"
    assert almost_equal(checkio([[1, 2], [3, 8], [9, 8], [7, 1]]), 40), "Quadrilateral"
    assert almost_equal(checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]), 26), "Pentagon"
    assert almost_equal(checkio([[7, 2], [3, 2], [1, 5], [3, 9], [7, 9], [9, 6]]), 42), "Hexagon"
    assert almost_equal(checkio([[4, 1], [3, 4], [3, 7], [4, 8], [7, 9], [9, 6], [7, 1]]), 35.5), "Heptagon"
