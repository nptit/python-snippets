import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"
VOWELS = 'aeiou'

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def vowels_percent(word):
    return 1.00 * len([c for c in word if c in VOWELS])/ len(word)

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    data = [vowels_percent(w) for w in wordList]
    #print data[:10], wordList[:10]
    pylab.hist(data, bins=numBins)

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
    #print vowels_percent('AAA')
