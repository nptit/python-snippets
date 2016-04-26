__author__ = 'qxu'

n2m={0:'m',1:'km',2:'Mm',3:'Gm',4:'Tm',5:'Pm',6:'Em',7:'Zm',8:'Ym'}
def meters(x):
    x='{0:0d}'.format(int(x))
    n,m=divmod(len(x),3)
    if m==0:
        n,m=n-1,m+3
    return x[:m]+n2m[n] if x[m:m+3]=='000' else (x[:m]+'.'+x[m:]).rstrip('0').rstrip('.')+n2m[n]

print meters(1)
print meters(12300000)
print meters(999999)
print meters(9000000000.0)
print meters(9e+24)