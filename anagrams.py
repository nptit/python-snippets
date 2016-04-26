
def anagram(word, wordlist):
    '''find all anagrams of word in the wordlist, return the longest anagram'''
    wletters = set(word)
    anagrams = [w for w in wordlist if wletters == set(w)]
    return max(anagrams, key = lambda x: len(x))

wordlist = ['stop', 'tops', 'stoops', 'spot', 'opts', 'post', 'pots']
word = 'stop'

print anagram(word, wordlist)
