from itertools import *
o=[(0,0)];golf=lambda h:min(sum(sum(((o+list(p))[i+1][j]-(o+list(p))[i][j])**2for j in[0,1])**0.5for i in range(5))for p in permutations(h))