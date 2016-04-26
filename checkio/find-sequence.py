def issame(l):
    'check whether the list elements are the same'
    return True if len(set(l)) == 1 else False

def match(mat):
    'check whether identical seq exists in rows/col/diag of square matrix'
    n = len(mat)

    for row in mat:
        if issame(row):
            return True

    for col in zip(*mat):
        if issame(col):
            return True

    diag1 = [mat[i][i] for i in range(n)]
    diag2 = [mat[i][n-i-1] for i in range(n)]
    return True if issame(diag1) or issame(diag2) else False

def submatrix(mat,i,j,m,n):
    'return a submatrix (dimension m n) of mat with up left corner @ i, j'
    submat = []
    for x in range(i, i+m):
        submat.append(mat[x][j:j+n])
    return submat

def checkio(matrix):
    'straightforward but somewhat clumsy solution'
    nrows = len(matrix)
    ncols = len(matrix[0])
    nsame = 4
    for i in range(nrows - nsame + 1):
        for j in range(ncols - nsame + 1):
            if match(submatrix(matrix, i, j, nsame, nsame)):
                return True
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 3],
        [1, 1, 2, 1],
        [1, 2, 1, 6],
        [1, 7, 2, 2]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
