def prob_white(marbles):
    "given the marbles, calculate the probability of getting white"
    lenf = float(len(marbles))
    return len([m for m in marbles if m == 'w'])/lenf

def checkio(marbles, step):
    'non recusive using a temp array'
    results = []
    results.append(tuple([marbles, 1.0]))

    for i in range(2, step + 1):
        tmp = []
        for e in results:
            r, p = e
            pw = prob_white(r)
            state1 = r.replace('b', 'w', 1)
            state1_prob = p*(1 - pw)
            state2 = r.replace('w', 'b', 1)
            state2_prob = p*pw
            tmp.append((state1, state1_prob))
            tmp.append((state2, state2_prob))
        results = tmp

    return round(sum([p * prob_white(r) for (r,p) in results]), 2)


def checkio(marbles, steps):
    'recursive implementation'

    pass

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u'bbw', 3) == 0.48, "1st example"
    assert checkio(u'wwb', 3) == 0.52, "2nd example"
    assert checkio(u'www', 3) == 0.56, "3rd example"
    assert checkio(u'bbbb', 1) == 0, "4th example"
    assert checkio(u'wwbb', 4) == 0.5, "5th example"
    assert checkio(u'bwbwbwb', 5) == 0.48, "6th example"
