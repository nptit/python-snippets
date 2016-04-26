'''sodoku solver using backtracking'''


def nextEmptyCell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return (-1, -1)

def row_nums(board, row):
    '''return values in row'''
    return [e for e in board[row] if e != 0]

def col_nums(board, col):
    '''return values in jrow'''
    return [e for e in zip(*board)[col] if e !=0]

def smsq_nums(board, row, col):
    '''return values that belongs to the small squares'''
    iblock, jblock = row // 3, col // 3
    nums = [board[3 * iblock + i][3 * jblock + j] for i in range(3) for j in range(3)]
    return [e for e in nums if e != 0]

def isValid(board, row, col, num):
    if num in row_nums(board, row):
        return False
    if num in col_nums(board, col):
        return False
    if num in smsq_nums(board, row, col):
        return False
    return True


def solveSodoku(board):
    row, col = nextEmptyCell(board)
    if row == -1:
        return True
    for num in range(1, 10):
        if isValid(board, row, col, num):
            board[row][col] = num
            if solveSodoku(board):
                return True
            board[row][col] = 0
    return False


def validNums(board, row, col):
    knowns = set(row_nums(board, row) + col_nums(board, col) + smsq_nums(board, row, col))
    return set(range(1,10)) - knowns


def solveSodoku(board):
    row, col = nextEmptyCell(board)
    if row == -1:
        return True

    for num in validNums(board, row, col):
        board[row][col] = num
        if solveSodoku(board):
            return True
        board[row][col] = 0
    return False



board = \
[[5, 1, 7, 6, 0, 0, 0, 3, 4],
 [2, 8, 9, 0, 0, 4, 0, 0, 0],
 [3, 4, 6, 2, 0, 5, 0, 9, 0],
 [6, 0, 2, 0, 0, 0, 0, 1, 0],
 [0, 3, 8, 0, 0, 6, 0, 4, 7],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 9, 0, 0, 0, 0, 0, 7, 8],
 [7, 0, 3, 4, 0, 0, 5, 6, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0]]

if __name__ == '__main__':
    from pprint import pprint
    print solveSodoku(board)
    pprint(board)








print "\n\nN Queen problem\n\n"


def isSafe(board, row, col):
    '''for Queen at row, col, check whether it is safe'''
    for i in range(col):
        if board[row][i]:
            return False

    # upper left corner
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # lower left corner
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True


def solveNqueen(board, col = 0):
    '''
    1) Start in the leftmost column
    2) If all queens are placed
        return true
    3) Try all rows in the current column.  Do following for every tried row.
        a) If the queen can be placed safely in this row then mark this [row,
            column] as part of the solution and recursively check if placing
         queen here leads to a solution.
       b) If placing queen in [row, column] leads to a solution then return
           true.
        c) If placing queen doesn't lead to a solution then umark this [row,
            column] (Backtrack) and go to step (a) to try other rows.
    4) If all rows have been tried and nothing worked, return false to trigger
        backtracking.
    '''
    if col >= len(board):
        return True

    for row in range(len(board)):
        if isSafe(board, row, col):
            board[row][col] = 1 # make change
            if solveNqueen(board, col+1):
                return True
            board[row][col] = 0 # unmake
    return False

if __name__ == '__main__':
    N = 8
    board=[[0]*N for _ in range(N)]
    solveNqueen(board)
    pprint(board)

