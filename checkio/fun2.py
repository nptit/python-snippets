

def getGuessedWord(secretWord, lettersGuessed):
    '''
    >>> secretWord = 'apple'
    >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    >>> print getGuessedWord(secretWord, lettersGuessed)
    '_ pp_ e'

    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    return ''.join(c if c in lettersGuessed else '_' for c in secretWord)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.

    >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    >>> print getAvailableLetters(lettersGuessed)
    abcdfghjlmnoqtuvwxyz

    '''
    # FILL IN YOUR CODE HERE...
    import string
    letters = string.letters[:26]
    return ''.join(c for c in letters if c not in lettersGuessed)

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)
