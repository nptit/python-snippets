import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.figure(1)
    pylab.hist(values, bins=numBins)
    if title:
      pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()


# Implement this -- Coding Part 2 of 2
def longestrun(values):
    'get the longest run number'
    count = values[:]
    count[0] = 1
    for i in range(1, len(values)):
      if values[i] == values[i-1]:
        count[i] = count[i - 1] + 1
      else:
        count[i] = 1
    return max(count)

def rolldices(die, numRolls):
    'given a die, roll it numRolls times, return the sequence of values'
    values = []
    for _ in range(numRolls):
        values.append(die.roll())
    return values

def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    nlongest = []
    for _ in range(numTrials):
        values = rolldices(die, numRolls)
        nlongest.append(longestrun(values))

    mean, std = getMeanAndStd(nlongest)
    makeHistogram(nlongest, 10, 'Trials', 'Longest run number')
    return mean


# die = Die([1,2,3,4])
# print rolldices(die, 10)
# One test case
# values = [1,2,3,4,5,6,7,1,2,3,4,5,6,1,2,1,4,5,6]
# makeHistogram(values, 3, 'x', 'y',title='title')
print getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)
