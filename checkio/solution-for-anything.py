class Cmp:
    def __init__(self, anything):
        pass
    def __cmp__(self, otherop):
        return True
    def __lt__(self, otherop):
        return True
    def __le__(self, otherop):
        return True
    def __gt__(self, otherop):
        return True
    def __ge__(self, otherop):
        return True
    def __eq__(self, otherop):
        return True
    def __ne__(self, otherop):
        return True

def checkio(anything):
    return Cmp(anything)

def checkio(anything):
    class T:
        __lt__=__gt__=__le__=__ge__=__eq__=__ne__ = lambda a, b: True
    return T()



if __name__ == '__main__':
    import re, math

    assert checkio({}) != [],         'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'

    print('NO WAY :(')
