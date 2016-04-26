import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals


pylab.figure(1)
pylab.plot(sorted(xVals), sorted(yVals))
#pylab.plot(sorted(xVals), yVals)
#pylab.plot(xVals, sorted(yVals))
#pylab.plot(xVals, yVals)
#pylab.plot(xVals, zVals)
pylab.show()
exit()

pylab.figure(1)
pylab.hist(tVals)
pylab.show()

pylab.figure(1)
pylab.hist(xVals)
pylab.show()

