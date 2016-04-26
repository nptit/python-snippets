from math import log, sqrt

def super_root(number):
    'solve log N - x log x = 0, note x log x is monotonically increasing'
    'so we can use binary search between 1 and N'
    l, r = 1.0, number

    cycles, maxcycles = 0, 10**6
    while cycles < maxcycles:
        cycles += 1
        guess = (l + r) / 2
        diff = log(number) - guess * log(guess)
        if diff < 0:
            r = guess
        else:
            l = guess

        if abs(diff) < 0.1 and abs(number - guess**guess) <= 0.001:
            return guess

    return guess


if __name__ == '__main__':

    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False
    assert check_result(super_root, 2), "Square"
    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"
    assert check_result(super_root, 9999999999), "10**10-1"
    assert check_result(super_root, 10**10), "10**10"
