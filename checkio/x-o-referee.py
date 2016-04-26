def checkio(game_result):
    rows = [tuple(r) for r in game_result]
    cols = zip(*game_result)
    diag = [tuple(r[i] for i,r in enumerate(rows)), tuple(r[2-i] for i,r in enumerate(rows))]
    combo = rows + cols + diag
    if any( [('O','O','O') == i for i in combo]):
        return 'O'
    if any( [('X','X','X') == i for i in combo]):
        return 'X'
    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"

