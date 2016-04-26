def binaryPrint(n):
    '''given integer n>0, print its bindary representaion'''
    if n <= 1:
        return str(n)
    n, r = divmod(n, 2)
    return binaryPrint(n) + str(r)

print binaryPrint(50)
