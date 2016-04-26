VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
import string, re

def is_striped(word):
    even = word[0::2]
    odd = word[1::2]
    if all([e in VOWELS for e in even]) and all([o in CONSONANTS for o in odd]):
        return True

    if all([o in VOWELS for o in odd]) and all([e in CONSONANTS for e in even]):
        return True

    return False

def checkio(text):
    words = [w.upper() for w in re.split(r'\s+|\.|\?|\!|,', text) if len(w) >= 2]
    return sum([1 for w in words if is_striped(w)])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name !is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
