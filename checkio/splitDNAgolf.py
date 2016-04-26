# 19 points, 70th
f=lambda s: len([1 for i,x in enumerate(s) for y in s[i+1:] if x > y])
def golf(t, n):
    l = [t[i:i+n] for i in range(0, len(t)-len(t)%n, n)]
    l1 = sorted(l, key=f)
    return ''.join(l1)



#55points 45th
golf=lambda t,n:''.join(sorted([t[i:i+n]for i in range(0,len(t)-len(t)%n,n)],key=lambda s:len([1for i,x in enumerate(s)for y in s[i+1:]if x>y])))


##19th place
golf=lambda t,n:''.join(sorted(map(''.join,zip(*[iter(t)]*n)),key=lambda s:len([1for i,x in enumerate(s)for y in s[i+1:]if x>y])))




print golf("ACGGCATAACCCTCGA",3) #"ACGCCCTAATCGGCA"
