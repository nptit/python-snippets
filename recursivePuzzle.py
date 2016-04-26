'''
5. A recursive puzzle
You have been given a puzzle consisting of a row of squares each containing an integer, like this:
3 6 4 1 3 4 2 5 3 0
The circle on the initial square is a marker that can move to other squares along the row. At each step
in the puzzle, you may move the marker the number of squares indicated by the integer in the square
it currently occupies. The marker may move either left or right along the row but may not move past
either end. For example, the only legal first move is to move the marker three squares to the right
because there is no room to move three spaces to the left.
The goal of the puzzle is to move the marker to the 0 at the far end of the row. In this configuration,
you can solve the puzzle by making the following set of moves:
3 6 4 1 3 4 2 5 3 0
3 6 4 1 3 4 2 5 3 0
3 6 4 1 3 4 2 5 3 0
3 6 4 1 3 4 2 5 3 0
3 6 4 1 3 4 2 5 3 0
3 6 4 1 3 4 2 5 3 0
3 6 4 1 3 4 2 5 3 0
Starting
position
Step 1:
Move right
Step 2:
Move left
Step 3:
Move right
Step 4:
Move right
Step 5:
Move left
Step 6:
Move right
Even though this puzzle is solvable - and indeed has more than one solution - some puzzles of this
form may be impossible, such as the following one:
3 1 2 3 0
In this puzzle, you can bounce between the two 3's, but you cannot reach any other squares.
Write a function bool Solvable(int start, Vector<int> & squares) that takes a starting
position of the marker along with the vector of squares. The function should return true if it is
possible to solve the puzzle from the starting configuration and false if it is impossible.
You may assume all the integers in the vector are positive except for the last entry, the goal square,
which is always zero. The values of the elements in the vector must be the same after calling your
function as they are beforehand, (which is to say if you change them during processing, you need to
change them back!)
bool Solvable(int start, Vector<int> & squares)
'''

def solve(start, vector):
    nv = len(vector)
    if vector[-1] != 0:
        raise ValueError("last element of the vector must be zero")

    if start < 0 or start >= len(vector):
        return False

    if start == len(vector) - 1:
        return True
    else:
        choices = [start + vector[start], start - vector[start]]
        choices = [c for c in choices if 0 <= c < nv]

        for newstart in choices:
            if solve(newstart, vector): return True
        return False

def solve(start, vector, path=None):
    if not path:
        path = []

    nv = len(vector)
    path += [start]

    if not vector:
        raise ValueError("vector is empty")
    if vector[-1] != 0:
        raise ValueError("last element of the vector must be zero")

    if start < 0 or start >= len(vector):
        return False

    if start == len(vector) - 1:
        print "path=", path
        return True
    else:
        choices = [start + vector[start], start - vector[start]]
        choices = [c for c in choices if 0 <= c < nv]

        if len(path) >=2:
            choices = [c for c in choices if c != path[-2]]

        for newstart in choices:
            if solve(newstart, vector, path): return True
        return False


print solve(0, [3, 6, 4, 1, 3, 4, 2, 5, 3, 0])
print solve(0, [3, 1, 2, 3, 1, 2, 0])
print solve(0, [3, 1, 2, 3, 0])
print solve(0, [1, 0, 1, 2, 3, 0])
print solve(0, [1, 0, 0])
