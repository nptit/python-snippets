from itertools import combinations

def checkio(words_set):
    is_suffix = lambda w1, w2: all([c1==c2 for c1, c2 in zip(w1[::-1], w2[::-1])])
    return any([is_suffix(w1, w2) for (w1, w2) in combinations(words_set, 2)])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #assert checkio({u"hello", u"lo", u"he"}) == True, "helLO"
    assert checkio({u"hello", u"la", u"hellow", u"cow"}) == False, "hellow la cow"
    exit()
    assert checkio({u"walk", u"duckwalk"}) == True, "duck to walk"
    assert checkio({u"one"}) == False, "Only One"
    assert checkio({u"helicopter", u"li", u"he"}) == False, "Only end"
