def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if not L:
        return float('NaN')
    l = [len(s) for s in L]
    N = len(l)
    mean = sum(l) / float(N)
    return (sum([(x - mean)**2 for x in l])/N)**0.5


print stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples'])
