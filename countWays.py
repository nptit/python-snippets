
'''
You're standing at the base of a staircase and are heading to the top. A small stride will move up one
stair, a large stride advances two. You want to count the number of ways to climb the entire staircase
based on different combinations of large and small strides. For example, a staircase of three steps
can be climbed in three different ways: via three small strides or one small stride followed by one
large stride or one large followed by one small. A staircase of four steps can be climbed in five
different ways (enumerating them is an exercise left to reader :-).
Write the recursive function int CountWays(int numStairs) that takes a positive numStairs
value and returns the number of different ways to climb a staircase of that height taking strides of
one or two stairs at a time.
Here's a hint about the recursive structure of the problem: consider the options you have at each stair.
You must either take a small stride or a large stride; either will take you closer to the goal and
therefore represents a simpler instance of the same problem that can be handled recursively. What is
the simplest possible situation and how is it handled?
int CountWays(int numStairs)
'''

def countWays(n):
    if n <= 1:
        return n
    else:
        return countWays(n-1) + countWays(n-2)

print countWays(1)
print countWays(2)
print countWays(10)

