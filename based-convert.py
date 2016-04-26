__author__ = 'qxu'


bin = '01'
oct = '01234567'
dec = '0123456789'
hex = '0123456789abcdef'
allow = 'abcdefghijklmnopqrstuvwxyz'
allup = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'



def fromBase(ns, basetable):
    ''' convert a base x to base 10, input is a string in base x '''
    base = len(basetable)
    return sum([ basetable.find(n)*base**i for i, n in enumerate(ns[::-1]) ])

def toBase(n, basetable):
    ''' base 10 to another base '''
    base = len(basetable)
    if n < base:
        return basetable[n]
    else:
        return toBase(n // base, basetable) + basetable[n % base]

def convert(ns, src_basetable, target_basetable):
    base10 = fromBase(ns, src_basetable)
    return toBase(base10, target_basetable)


convert("15", dec, bin)
convert("15", dec, oct)
convert("1010", bin, dec) #should return "10"
print convert("1010", bin, hex) #should return "a"
