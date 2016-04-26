def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    c = char.lower()
    vowels = 'aeiou'
    i = 0
    while i < 5:
        if c == vowels[i]:
            return True
        i += 1

    return False


def isVowel(char):
    char = char.lower()
    vowels = 'aeiou'
    return any(map(lambda x: char == x, vowels))

print isVowel('n')
