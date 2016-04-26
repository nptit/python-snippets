import itertools
from collections import Counter
from copy import deepcopy

def isvalidmsq(lol):
    'given a square, check whether it is a magic squre'
    n = len(lol)

    mc = n * (n * n + 1) / 2
    sums = [sum(r) for r in lol] + [sum(c) for c in zip(*lol)] + \
        [sum([lol[i][i] for i in range(n)]), sum([lol[i][n -1 - i] for i in range(n)])]

    return True if all([s == mc for s in sums]) else False

def one_replace(comb, lol):
    l = deepcopy(lol)
    idx = 0
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][j] == 0:
                l[i][j] = comb[idx]
                idx += 1
    return l

def checkio(lol):
    'given list of list, replace 0s to form a magic square, brute force method '
    '-- exponential too slow for n >= 10'
    n = len(lol)
    n_all = set(range(1, n**2 + 1))
    n_used = set([i for r in lol for i in r if r != 0])
    n_notused = n_all - n_used
    for cb in itertools.permutations(n_notused):
        l = one_replace(cb, lol)
        if isvalidmsq(l):
            return l
    return []

def singletons(lol):
    'solve the simplest cases in which one row, col, or diagonal has only one unknown'
    n = len(lol)
    mc = n * (n * n + 1) / 2
    rows = lol
    cols = zip(*lol)
    dia1 = [lol[i][i] for i in range(n)]
    dia2 = [lol[i][n -1 - i] for i in range(n)]


    print rows, cols, dia1, dia2

def solverow(row):
    'solve a row/col/diag with only one unknown'
    n = len(row)
    mc = n * (n**2 + 1) / 2
    ones = [i for i, e in enumerate(row) if e == 0]
    if len(ones) == 1:
        row[ones[0]] = mc - sum(row)
    return row


if __name__ == '__main__':
    #This part is using only for self-testing.
    print solverow([4,3,0])
    print solverow([13,0,2, 3])
    singletons([[2, 7, 6], [9, 5, 1], [4, 3, 0]])
    exit()

    def check_solution(func, in_square):
        SIZE_ERROR = "Wrong size of the answer."
        MS_ERROR = "It's not a magic square."
        NORMAL_MS_ERROR = "It's not a normal magic square."
        NOT_BASED_ERROR = "Hm, this square is not based on given template."
        result = func(in_square)
        #check sizes
        N = len(result)
        if len(result) == N:
            for row in result:
                if len(row) != N:
                    print(SIZE_ERROR)
                    return False
        else:
            print(SIZE_ERROR)
            return False
        #check is it a magic square
        # line_sum = (N * (N ** 2 + 1)) / 2
        line_sum = sum(result[0])
        for row in result:
            if sum(row) != line_sum:
                print(MS_ERROR)
                return False
        for col in zip(*result):
            if sum(col) != line_sum:
                print(MS_ERROR)
                return False
        if sum([result[i][i] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False
        if sum([result[i][N - i - 1] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False

        #check is it normal ms
        good_set = set(range(1, N ** 2 + 1))
        user_set = set([result[i][j] for i in range(N) for j in range(N)])
        if good_set != user_set:
            print(NORMAL_MS_ERROR)
            return False
        #check it is the square based on input
        for i in range(N):
            for j in range(N):
                if in_square[i][j] and in_square[i][j] != result[i][j]:
                    print(NOT_BASED_ERROR)
                    return False
        return True


    assert check_solution(checkio,
                          [[2, 7, 6],
                           [9, 5, 1],
                           [4, 3, 0]]), "1st example"

    assert check_solution(checkio,
                          [[0, 0, 0],
                           [0, 5, 0],
                           [0, 0, 0]]), "2nd example"

    assert check_solution(checkio,
                          [[1, 15, 14, 4],
                           [12, 0, 0, 9],
                           [8, 0, 0, 5],
                           [13, 3, 2, 16]]), "3rd example"
    print checkio([[1, 15, 14, 4],
                           [12, 0, 0, 9],
                           [8, 0, 0, 5],
                           [13, 3, 2, 16]])
    n = 4
    print checkio([[0]*n  for _ in range(n)])
