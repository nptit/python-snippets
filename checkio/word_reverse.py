'reverse words in string'

import re


def reverse_words(sentence):
    words = re.findall(r'\w+', sentence)
    puncs = re.findall(r'\W+', sentence)
    return ''.join([a+b if a.isdigit() else a[::-1]+b for (a, b) in zip(words, puncs)])


#s = 'I have 36 books, 40 pens2.'
#print reverse_words(s)


def reverse_words(sentence):
    i, r, w = 0, [], ''
    while i < len(sentence):
        c =sentence[i]
        if c in '. ,0123456789':
            r.append(w[::-1])
            r.append(c)
            w = ''
        else:
            w += c
        i += 1
    return ''.join(r)


s = 'I have 36 books,  .40 pens2.'
print s
print reverse_words(s)



def reverse_words(sentence):
    return ''.join([w[::-1] if w.isalnum() and not w.isdigit() else w for w in re.split(r'(\w+)', sentence)])



s = 'I have 36 books,  .40 pens2.'
print s
print reverse_words(s)



