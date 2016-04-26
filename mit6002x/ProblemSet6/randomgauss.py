import random
import pylab

data = []
nsample = 5000
for i in range(nsample):
    x = random.gauss( 50,10) + random.gauss( 70, 10 )
    data.append(x)


pylab.figure(1)
pylab.hist(data)
pylab.show()
