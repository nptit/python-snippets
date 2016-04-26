
for i in range(1,13):
    for j in range(1,13):
        print "{:4d}".format(i*j),
    print


def fib(n):
    if n in [0,1]:
        return n
    return fib(n-1) + fib(n-2)

for i in range(10):
    print fib(i)

def fib1():
    a = 0
    b = 1
    while True:
        yield a
        b, a = a+b, b

def fib2():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a+b


g1= fib1()
print g1.next(), g1.next(), g1.next()

g2= fib2()
print g2.next(), g2.next(), g2.next()


import re

phone=re.compile(r"\({0,1}\d{3}\){0,1}-\d{3}-\d{4}")

text = "xx 123-456-0000, 123-000-456 (132)-456-0000"
print re.findall(phone, text)

text ="foo (bar ( new Point(x, graph.getY()) ));"
print text.replace("(", " ( ").replace(")", " ) ")


n = 0b11101111

print n & 1
for i in range(9):
    print n & (1<<i)
