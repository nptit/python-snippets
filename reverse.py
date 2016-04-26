def reverse(s):
    return ''.join(s[i] for i in range(len(s)-1, -1, -1))

#print reverse('123abc')

def titleCase(title):
    special_words = ['a', 'and', 'in', 'the', 'at', 'but', 'or', 'to', 'with']
    words = title.split()
    cap_words = [w.capitalize() for w in words]
    t_words = [x.lower() if x.lower() in special_words and i not in [0, len(cap_words)-1] else x for i,x in enumerate(cap_words) ]
    return ' '.join(t_words)

def titleCase(title):
    special_words = ['a', 'and', 'in', 'the', 'at', 'but', 'or', 'to', 'with']
    words = title.split()
    cap_words = [w.capitalize() for w in words]
    t_words = list(w.lower() if w.lower() in special_words else w for w in cap_words[1:-1])
    return ' '.join([cap_words[0]] + t_words + [cap_words[-1]])

def titleCase(title):
    import string
    d = {u:c for u, c in zip(string.uppercase, string.lowercase)}

    def lower(word):
        return ''.join(d[c] if c in d else c for c in word)

    def capitalize(word):
        if not word:
            return word

        w = lower(word)
        first = w[0]
        for k, v in d.items():
            if v == w[0]:
                first = k
                break
        return first+w[1:]

    title = lower(title)
    special_words = ['a', 'and', 'in', 'the', 'at', 'but', 'or', 'to', 'with']
    words = title.split()
    result = []
    for i in range(len(words)):
        wi = words[i]
        if i in [0, len(words) -1]:
            result.append(capitalize(wi))
        else:
            if lower(words[i]) not in special_words:
                result.append(capitalize(wi))
            else:
                result.append(wi)
    return ' '.join(result)


# print titleCase('')==''

# print titleCase('a Box in a tree')
# #
# assert titleCase('a Box in a tree') == 'A Box in a Tree'


def int2bin(n):
    '''convert base 10 int into binary string'''
    if n == 0:
        return str(n)
    n, r = divmod(n, 2)
    return int2bin(n) + str(r)

print int2bin(161)
