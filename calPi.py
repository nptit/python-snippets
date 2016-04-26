
import random
import math

def pointGenerator():
    scale = 2.
    while True:
        x = scale * random.random() - 1.0
        y = scale * random.random() - 1.0
        yield (x, y)

def areaRatio():
    '''calculate ratio of area of a circle inside a square'''
    return math.pi/4.0

def inCircle(point):
    x, y = point
    return math.sqrt(x*x+y*y) < 1.0


nTry = 100
nCircle = 0
nSquare = 0


for point in pointGenerator():
    nSquare += 1
    if inCircle(point):
        nCircle += 1
    if nSquare > nTry:
        break

print 'pi = ', 100*abs(4.0*nCircle/nSquare - math.pi)/math.pi
