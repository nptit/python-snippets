__author__ = 'qxu'

def unique_in_order(iterable):
    # time complexity O(n), space complexity O(n)
    lst=[]
    count=0
    for i in iterable:
        if len(lst) >= 1:
            if i != lst[-1]:
                lst.append(i)
                count += 1
        else:
            lst.append(i)
            count += 1
    return lst




assert(unique_in_order('AAAABBBCCDAABBB')==['A','B','C','D','A','B'])