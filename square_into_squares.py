# -*- coding: UTF-8 -*-
'''

Task

Given a positive integral number n, return a strictly increasing sequence
(list/array/string depending on the language) of numbers, so that the sum of the
squares is equal to n².

If there are multiple solutions (and there will be), return the result with the
largest possible values:

Examples

decompose(11) must return [1,2,4,10]. Note that there are actually two ways to
decompose 11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't
return [2,6,9], since 9 is smaller than 10.

For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since [1,
1, 4, 9, 49] doesn't form a strictly increasing sequence.

decompose 50 `shouldBe` Just [1,3,5,8,49]
decompose 4  `shouldBe` Nothing
Note

Neither [n] nor [1,1,1,…,1] are valid solutions. If no valid solution exists,
return nil, null, Nothing, None or "".

The function "decompose" will take a positive integer n and return the
decomposition of N = n² as:

[x1 ... xk]

Hint

Very often xk will be n-1.
'''

import math


def decompose(n):
    def _recurse(s, i):
        if s < 0:
            return None

        if s == 0:
            return []

        for j in xrange(i - 1, 0, -1):
            sub = _recurse(s - j ** 2, j)
            if sub != None:
                return sub + [j]

    return _recurse(n ** 2, n)


import math


def decompose(n, s=None):
    if not s:
        s = n * n

    m = int(math.sqrt(s))

    if m * m == s and m != n:
        return [m]

    for i in range(min(n, int(math.ceil(math.sqrt(s)))) - 1, 1, -1):
        sol = decompose(i, s - i * i)
        if sol:
            return sol + [i]


print decompose(50)
