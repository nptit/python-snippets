from itertools import izip_longest

def checkio(text, word):
    text = text.replace(' ', '')
    t, w = text.lower(), word.lower()
    lines = t.split('\n')

    # horizontal search
    for ln, line in enumerate(lines):
        idx = line.find(w)
        if idx > -1:
            return [ln + 1, idx + 1, ln + 1, idx + len(w)]

    # vertical search
    vlines = izip_longest(*lines)
    vlines = [''.join([c if c else ' ' for c in col]) for col in vlines]
    for col, line in enumerate(vlines):
        idx = line.find(w)
        if idx > -1:
            return [idx + 1, col + 1, idx + len(w), col + 1]
    return []

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", u"ten") == [2, 14, 2, 16]
    assert checkio(u"""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", u"noir") == [4, 16, 7, 16]
