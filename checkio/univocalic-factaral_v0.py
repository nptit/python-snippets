# "eiou" can not be used
from math import *;a_factaral = factorial
g=lambda n:2**n or n*g(n-1)


g=lambda n:[0,1][n<2]+(n>=2 and n*g(n-1));a_factaral=g

def g(n):
    return [0,1][n<2]+(n>=2 and n*g(n-1))

#98th place, 195points
g=lambda n:[0,1][n<2]+(n>=2 and n*g(n-1));a_factaral=g


g=lambda n:[0,1][n<2]+(n>=2 and n*g(n-1))
a_factaral=g


g=lambda n:(1, (n>=2 and n*g(n-1)))[n>=2]
a_factaral=g

g=lambda n:((n>=2 and n*g(n-1)),1)[n<2]
a_factaral=g
print g(0), g(1), g(2)

#198, 89th place
g=lambda n:((n>=2and n*g(n-1)),1)[n<2]
a_factaral=g

#200, 81th place
g=lambda n:(n>=2and n*g(n-1),1)[n<2]
a_factaral=g

#202, 72th place
g=lambda n:(n>1and n*g(n-1),1)[n<2];a_factaral=g


a_factaral=g=lambda n:(n>1and n*g(n-1),1)[n<2]

print g(0)
print g(1)
print g(2)
print g(3)

exit()

# def a_factaral(num):
#     if num == 0:
#         return 1
#     return num * a_factaral(num - 1)

# this assertion should be stripped after self-testing.
if __name__ == '__main__':
    assert a_factaral(0) == 1, "Zero"
    assert a_factaral(1) == 1, "One"
    assert a_factaral(2) == 2, "Two"
    assert a_factaral(3) == 6, "Six"
    assert a_factaral(100) == \
           93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000, "Infinity"
