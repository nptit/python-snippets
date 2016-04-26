a=[0,1,2,3,4,5,6,7,8]
b=[5,10,10,10,15]
c=[0,1,2,4,6,8]
d=[6,7,11,12,13,15]
e=[9,0,0,3,3,3,6,6]

def mean(l):
    return sum(l)*1.0/len(l)

def var(l):
    m = mean(l)
    return 1.0*sum((x-m)**2 for x in l) / len(l)

l=[a,b,c,d,e]

# for e in l:
#     print mean(e)
#     print var(e)

def possible_mean(L):
    return sum(L)/len(L)

def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return temp / len(L)

for e in l:
    print possible_mean(e)


for e in l:
    print e, possible_variance(e)


