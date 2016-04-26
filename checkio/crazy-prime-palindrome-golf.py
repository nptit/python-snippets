# def golf(n):
#  for i in range(n+1,7**6):
#   if all([i%k!=0 for k in range(2,i)]) and str(i)==str(i)[::-1]:return i

# golf=lambda n:[i for i in range(n+1,7**6) if str(i)==str(i)[::-1] and all([i%k!=0 for k in range(2,i)])][0]


# golf=lambda n:[i for i in range(n+1,7**6) if str(i)==str(i)[::-1] and all(i%k!=0 for k in range(2,i))][0]


# r=range;golf=lambda n:[i for i in r(n+1,7**6)if str(i)==str(i)[::-1]and all(i%k!=0 for k in r(2,i))][0]

#golf=lambda n:[i for i in range(n+1,7**6)if str(i)==str(i)[::-1]and all(i%k!=0for k in range(2,i))][0]

#golf=lambda n:[i for i in range(n+1,7**6)if str(i)==str(i)[::-1]and all(i%k for k in range(2,i))][0]

#golf=lambda n:[i for i in range(n+1,7**6)if str(i)==str(i)[::-1]and all(i%k for k in range(2,i))][0]


#golf=lambda n:[i for i in range(n+1,7**6)if str(i)==str(i)[::-1]and all(i%k for k in range(2,i))][0]

#r=range;golf=lambda n:[i for i in r(n+1,7**6)if str(i)==str(i)[::-1]and all(i%k for k in r(2,i))][0]


#import sympy;golf=lambda n:[i for i in range(n+1,7**6)if str(i)==str(i)[::-1]and sympy.isprime(i)][0]

#import sympy;golf=lambda n:[i for i in sympy.primerange(n+1,7**6)if str(i)==str(i)[::-1]][0]

#golf=lambda n:[i for i in range(n+1,7**6)if str(i)==str(i)[::-1]and all(i%k for k in range(2,i))][0]

#golf=lambda n:2if n<2 else[x for x in range(n+1,7**6)if str(x)==str(x)[::-1]and 2**x%x==2][0]

golf=lambda n:2if n<2else[x for x in range(n+1,7**6)if str(x)==str(x)[::-1]and 2**x%x==2][0]

golf=lambda n:[x for x in range(n+1,7**6)if str(x)==str(x)[::-1]and(2**x%x==2or x==2)][0]

def golf(n):return[x for x in range(n+1,7**6)if str(x)==str(x)[::-1]and(2**x%x==2or x==2)][0]

golf=lambda n:[x for x in range(n+1,7**6)if `x`==`x`[::-1]and(2**x%x==2or x==2)][0]

golf=lambda n:[x for x in range(n+1,7**6)if `x`==`x`[::-1]*(2**x%x==2or x==2)][0]

golf=lambda n:[x for x in range(n+1,7**6)if `x`==`x`[::-1]*(~-2**x%x<2)][0]
golf=lambda n:[x for x in range(n+1,7**6)if`x`[::-1]==`x`*(~-2**x%x<2)][0]

def golf(n):
 while n:
  n+=1
  if`n`[::-1]==`n`*(~-2**n%n<2):return n


print golf(1)
print golf(2)
print golf(101)
