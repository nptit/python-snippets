__author__ = 'qxu'

def addsup(a1, a2, a3):
    # given arrays a1,a2,a3, find all triplets of a1, a2 and a3 such that a1[i]+a2[j]=a3[k]
    return [[x,y,z] for x in a1 for y in a2 for z in a3 if x+y-z==0]
