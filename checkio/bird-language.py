VOWELS = "aeiouy"

def wordconv(w):
    'translate a word'
    i, result = 0, []
    while i < len(w):
        c = w[i]
        result.append(c)
        if c in VOWELS:
            i += 3
        else:
            i += 2

    return ''.join(result)

def translate(phrase):
    'translate a phrase'
    return ' '.join([wordconv(w) for w in phrase.split()])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate(u"hieeelalaooo") == "hello", "Hi!"
    assert translate(u"hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate(u"aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate(u"sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
