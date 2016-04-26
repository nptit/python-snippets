
def isPalindrome(s):
    return s == s[::-1]

def substr(s):
    n = len(s)
    return [s[i:j] for i in range(n) for j in range(i+1, n+1)]

def longestPalindromeSub(s):
    '''given string s, return the longest palindromic sub string'''
    return sorted([sub for sub in substr(s) if isPalindrome(sub)], key = lambda x: len(x))[-1]




print substr('abc')
print longestPalindromeSub('abcdzdcab')
