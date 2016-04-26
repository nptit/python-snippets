import pylab
import random
import numpy as np
import scipy as sp
from scipy.interpolate import interp1d
from scipy import interp

x = range(100)
y = [random.random() * 100 for _ in x]
fit = np.polyfit(x, y, 10)
poly = np.poly1d(fit)

f = interp1d(x,y, kind='linear')
fpred = f(x)
print f(10)

ypred = [poly(i) for i in x]

pylab.figure(1)
pylab.plot(x,y)
pylab.plot(x,ypred, 'o-', color ='r')
pylab.plot(x,fpred, 'o-', color ='g')
pylab.show()
