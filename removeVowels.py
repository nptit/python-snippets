def removeVowels(s):
    '''remove vowels from string s, recursively'''
    if len(s) <=1:
        if s in 'aeiouAEIOU' or not s:
            return ''
        else:
            return s

    middle = len(s) // 2
    s1 = s[:middle]
    s2 = s[middle:]
    print s1, s2
    return removeVowels(s1) + removeVowels(s2)

print removeVowels('abcabc')
