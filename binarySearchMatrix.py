def searchArray(arr, target):
    '''assuming incremental array'''
    start, end = 0, len(arr) - 1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == target:
            return middle
        elif target > arr[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return None

# if __name__ == '__main__':
#     l = [1,2,3,4,5, 6]
#     l = [1,2,8]
#     print searchArray(l, 2)

def searchArray(arr, target, start, end):
    if start > end:
        return None

    midIndex = (start+end) // 2
    arrMid = arr[midIndex]
    if target == arrMid:
        return midIndex
    elif target > arrMid:
        return searchArray(arr, target, midIndex+1, end)
    else:
        return searchArray(arr, target, start, midIndex-1)


# if __name__ == '__main__':
#     l = [1,2,3,4,5, 6]
#     l = [1,2,7,8,0]
#     l = []
#     print searchArray(l, 8, 0, len(l)-1)

def outOfBound(arr, index):
    '''check whether array[index] is out of bound'''
    try:
        arr[index]
    except IndexError:
        return True
    return False


def binarySearchNoLength(arr, num):
    '''
    Given a sorted array of unknown length
    and a number to search for, return the index of the number in the array.
    Accessing an element out of bounds throws exception. If the number occurs
    multiple times, return the index of any occurrence. If it isn't present, return
    -1. - See more at: http://www.ardendertat.com/2011/11/21/programming-interview-
    questions-17-search-unknown-length-array/#sthash.CyXTntUS.dpuf
    '''
    #check array indexes 0, 2^0, 2^1, 2^2, ...
    index, exp = 0, 0
    while True:
        try:
            if arr[index]==num:
                return index
            elif arr[index]<num:
                index=2**exp
                exp+=1
            else:
                break
        except IndexError:
            break

    #Binary Search
    left=(index/2)+1
    right=index-1
    while left<=right:
        try:
            mid=left+(right-left)/2
            if arr[mid]==num:
                return mid
            elif arr[mid]<num:
                left=mid+1
            else:
                right=mid-1
        except IndexError:
            right=mid-1
    return -1

print binarySearchNoLength([1,2,3], 9)



def searchMatrix(mat, target, rowStart, rowEnd, colStart, colEnd):
    '''
    Problem Statement

    Write an efficient algorithm that searches for a value in an m x n matrix.
    This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
    Example

    Consider the following matrix:
    [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    Given target = 3, return true.
    Challenge

    O(log(n) + log(m)) time
    '''


    if rowStart > rowEnd or colStart > colEnd:
        return None

    midRow = (rowStart + rowEnd) // 2
    # complexity for this implementation is log(m)*log(n)
    col = searchArray(mat[midRow], target, colStart, colEnd)
    if col is not None:
        return midRow, col

    if target < mat[midRow][0]:
        return searchMatrix(mat, target, rowStart, midRow-1, colStart, colEnd)
    elif target > mat[midRow][0]:
        return searchMatrix(mat, target, midRow+1, rowEnd, colStart, colEnd)


# if __name__ == '__main__':
#     mat = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
#     print searchMatrix(mat, 3, 0, len(mat)-1, 0, len(mat[0])-1)



