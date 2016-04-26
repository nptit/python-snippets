from string import punctuation
import re


def sim(w1, w2):
    'calculate similarity between two words'
    s = 0
    if w1[0] == w2[0]:
        s += 10.

    if w1[-1] == w2[-1]:
        s += 10.

    s += 30. * min(len(w1), len(w2))/max(len(w1), len(w2))
    s += 50. * len(set(w1) & set(w2)) / len(set(w1) | set(w2))
    return s

def avgsim(w, ws):
    'calculate avg similarity between a words and a word list'
    #return sum([sim(w, w2) for w2 in ws])/len(ws)
    'corrected for w is repeated in ws'
    return (sum([sim(w, w2) for w2 in ws]) - 100)/(len(ws) - 1)


def find_word(message):
    rx = re.compile(r'[\s{}]+'.format(re.escape(punctuation)))
    ws = [w.lower() for w in re.split(rx, message) if w]
    sims = [avgsim(w, ws) for w in ws]
    mx = max(sims)
    # get all indices with max and return the last one
    idx = [i for i, s in enumerate(sims) if s == mx]
    return ws[idx[-1]]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #print sim('friend','ted')
    #print avgsim('friend', ['friend', 'friend','and', 'fred', 'ted'])
    print find_word("Speak friend and enter.")
    print find_word(u"Beard and Bread") #== "bread", "Bread is Beard"

    assert find_word(u"Speak friend and enter.") == "friend", "Friend"

    assert find_word(u"The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     u"I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word(u"Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     u" According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word(u"One, two, two, three, three, three.") == "three", "Repeating"
