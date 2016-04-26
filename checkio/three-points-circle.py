import re
import math

def roundx(r):
    return int(r) if abs(r-int(r)) < 0.01 else round(r, 2)

def checkio(data):
    # rx = re.compile(r'(\d+,\d+)')
    # xy = [x.split(',') for x in re.findall(rx, data)]
    # (x1, y1), (x2, y2), (x3, y3) = [(float(x), float(y)) for (x, y) in xy]
    (x1, y1), (x2, y2), (x3, y3) = eval('[' + data +']')
    # solve for x0, y0 analytically
    tx = (x2**2 - x1**2 + y2**2 - y1**2)*(-y1 + y3) - (x3**2 - x1**2 + y3**2 - y1**2)*(-y1 + y2)
    bx = (-x1 + x2)*(-y1 + y3) - (-x1 + x3)*(-y1 + y2)
    x0 = tx / (2 * bx)

    ty = (x2**2 - x1**2 + y2**2 - y1**2)*(-x1 + x3) - (x3**2 - x1**2 + y3**2 - y1**2)*(-x1 + x2)
    by = (-y1 + y2)*(-x1 + x3) - (-y1 + y3)*(-x1 + x2)
    y0 = ty / (2 * by)

    r = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

    return '(x-{})^2+(y-{})^2={}^2'.format(roundx(x0), roundx(y0), roundx(r))

    # brute force via grid search
    # xy = [(float(x), float(y)) for (x, y) in xy]
    # eqs = lambda x0, y0: [(x0 - p[0])**2 +(y0 - p[1])**2 for p in xy]
    # for x0 in range(1000):
    #     for y0 in range(1000):
    #         a = x0 / 100.
    #         b = y0 / 100.
    #         eq = eqs(a, b)
    #         if abs(eq[0] - eq[1]) <= 0.05 and abs(eq[0] - eq[2]) <= 0.05:
    #             r = math.sqrt(eq[0])
    #             a, b, r = roundx(a), roundx(b), roundx(r)
    #             return '(x-{})^2+(y-{})^2={}^2'.format(a, b, r)



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print checkio(u"(2,2),(4,2),(2,4)")
    print checkio(u"(7,7),(4,3),(1,8)")
    exit()
    assert checkio(u"(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio(u"(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
