
def genPrimes():
    primers = []
    i = 1
    while True:
        i = i + 1
        for d in primers:
            if i % d == 0:
                break
        else:
            primers.append(i)
            yield i

gen = genPrimes()

for i in range(1000):
    p = gen.next()
    if i % 100 == 0:
        print p




