# too slow!
from itertools import*
def golf(m):
 n=len(m);x=range;d=[]
 for r in x(2,n+1):
  for p in permutations(x(n), r):
   if p[0]==0 and p[-1]==n-1 and all([m[p[i-1]][p[i]]>0 for i in x(1,len(p))]):
    d.append(sum([m[p[i-1]][p[i]] for i in x(1,len(p))]))
 return min(d) if d else 0


print golf(((0, 80, 58, 0), (80, 0, 71, 80), (58, 71, 0, 58), (0, 80, 58, 0))) == 116

