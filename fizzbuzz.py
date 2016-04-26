
def fizzbuzz(n):
    if n % 15 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return n

for i in range(20):
    print fizzbuzz(i)


def permutation(s):
    if len(s) <= 1:
        return [s]
    elif len(s) == 2:
        return [s, s[::-1]]
    result = []
    for i in range(len(s)):
        char = s[i]
        substr = s[0:i] + s[i+1:]
        ps = permutation(substr)
        for p in ps:
            news = char + p
            result.append(news)

    return result

print len(permutation('abcd'))

