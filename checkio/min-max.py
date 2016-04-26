import types

def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1 and isinstance(args[0], (list, tuple, set, types.GeneratorType, str)):
        data = list(args[0])
    else:
        data = args

    if key:
        curr_max = key(data[0])
    else:
        curr_max = data[0]

    curr_ind = 0


    for i, e in enumerate(data):
        v = e
        if key:
            v = key(e)
        if v > curr_max:
            curr_max = v
            curr_ind = i

    return data[curr_ind]


def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1 and isinstance(args[0], (list, tuple, set, types.GeneratorType, str)):
        data = list(args[0])
    else:
        data = args

    if key:
        curr_min = key(data[0])
    else:
        curr_min = data[0]

    curr_ind = 0

    for i, e in enumerate(data):
        v = e
        if key:
            v = key(e)
        if v < curr_min:
            curr_min = v
            curr_ind = i

    return data[curr_ind]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert min(3, 2) == 2, "Simple case min"

    assert max(3, 2) == 3, "Simple case max"

    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
