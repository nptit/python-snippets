__author__ = 'qxu'

""" You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

    next_bigger(12)==21
    next_bigger(513)==531
    next_bigger(2017)==2071
    If no bigger number can be composed using those digits, return -1:

    next_bigger(9)==-1
    next_bigger(111)==-1
    next_bigger(531)==-1
"""

from itertools import permutations

def next_bigger_v1(num):
    digits = tuple([c for c in str(num)])
    seq = sorted(permutations(digits, r=len(digits)), key=lambda x: tuple(x))
    seq = unique_list(seq)
    for i, s in enumerate(seq):
        if digits == s and i+1 < len(seq):
            return int("".join(seq[i+1]))
    return -1


def unique_list(sorted_lst):
    out = [sorted_lst[0]]
    out.extend([v for i, v in enumerate(sorted_lst[1:]) if v != sorted_lst[i]])
    return out


def next_bigger(num):
    digits = [c for c in str(num)]
    for i in range(len(digits)-2, -1, -1):
        if digits[i] < digits[i+1]:
            digits = digits[:i+1]+sorted(digits[i+1:])
            for j, v in enumerate(digits[i+1:]):
                if digits[j+i+1] > digits[i]:
                    digits[i], digits[j+i+1] = digits[j+i+1], digits[i]
                    return int("".join(digits))

    return -1


print next_bigger(2170)
print next_bigger(534976)
print next_bigger(983)
print next_bigger(19000)
