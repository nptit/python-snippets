def reverseString(s):
    ''' How can you reverse a string without dynamic memory allocation or temporary variables (aside from indexer).'''
    n = len(s)
    for i in range(n//2):
        s[i], s[n-1-i] = s[n-1-i], s[i]


s= [1,2]
reverseString(s)
print s
