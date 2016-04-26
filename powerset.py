__author__ = 'qxu'


def power(lst):
    # generate a power set recusively
    if not lst:
        return []
    if len(lst) == 1:
        return [[],lst]
    p1=power(lst[:-1])
    return p1+[el+[lst[-1]] for el in p1]

print power([1,2])
print power([1,2,3])
