def checkio(matrix):
    # -A = A.transpose
    A = [e for row in matrix for e in row]
    T = [e for row in zip(*matrix) for e in row]
    return all([-a == t for a, t in zip(A, T)])

checkio = lambda m: (m == [[-x for x in row] for row in list(zip(*m))])



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
