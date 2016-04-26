__author__ = 'qxu'



def strStr(p, t):
    print "called 2"
    for i in xrange(len(t)-len(p)+1):
        if p == t[i:i+len(p)]:
            return i
    return -1

def strStr(p, t):
    print "called 1"
    return t.find(p)

p="21123"
t="332123"

print strStr(p,t)