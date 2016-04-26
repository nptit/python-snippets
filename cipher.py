
import string

def cipher(s, k):
    '''cesaer's cipher, shift the message by k'''
    letters = string.ascii_lowercase
    uc_letters = letters.upper()
    ciphertext = ''
    for c in s:
        if c not in uc_letters + letters:
            ciphertext += c
        else:
            idx = letters.index(c.lower())
            new_idx = (idx + k) % len(letters)
            if c in letters:
                ciphertext += letters[new_idx]
            elif c in uc_letters:
                ciphertext += uc_letters[new_idx]

    return ciphertext

def cipher(s, k):
    '''cesaer's cipher, shift the message by k'''
    letters = string.ascii_lowercase

    ciphertext = ''
    for c in s:
        lc = c.lower()
        if lc not in letters:
            ciphertext += c
        else:
            idx = letters.index(lc)
            new_idx = (idx + k) % len(letters)
            newc = letters[new_idx]
            if c.isupper():
                ciphertext += newc.upper()
            else:
                ciphertext += newc

    return ciphertext


print cipher('Hello, World!', 5)
print cipher('', 5)


def makedict(shift):
    letters = string.ascii_lowercase
    d = dict((c, letters[(letters.index(c) + shift) % len(letters)]) for c in letters)
    d.update((k.upper(), v.upper()) for k,v in d.items())
    return d

print makedict(0)


def apply_shift(s, shift):
    d = makedict(shift)
    return ''.join(d[c] if c in d else c for c in s)

#print apply_shift('z', 1)

