from collections import Counter

def checkio(first, second):
    c1 = Counter(first.split(','))
    c2 = Counter(second.split(','))
    return ','.join(sorted((c1 & c2).keys()))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"hello,world", u"hello,earth") == "hello", "Hello"
    assert checkio(u"one,two,three", u"four,five,six") == "", "Too different"
    assert checkio(u"one,two,three", u"four,five,one,two,six,three") == "one,three,two", "1 2 3"
