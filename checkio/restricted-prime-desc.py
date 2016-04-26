''' check for prime without using: This crazy calculator has learned new some
words (but forgotten some others) and does not accept new words, certain symbols
and it hates digits!

The list of forbidden words and symbols:

    import div eval range len / % - digits (0-9)

Given a number (0 < n < 10000), you should check if it is a prime or not. Your
solution should not contain any of the forbidden words, symbols or digits (even
as a part of another word).

Input: A number as an integer.

Output: Is it prime or not as a boolean.'''

def checkio(n):
    one = sum([True])
    two = sum([True, True])
    i = two
    while i < n:
        new = i
        while True:
            if n == new:
                return False
            if new > n:
                break
            new += i
        i += one
    return True

