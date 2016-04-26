import string


def checkio(data):
    d = [c for c in data if c in string.digits]
    lc = [c for c in data if c in string.letters[:26]]
    uc = [c for c in data if c in string.letters[-26:]]

    return all([len(data) >= 10, len(d) >= 1, len(lc) >= 1, len(uc) >= 1])

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"
