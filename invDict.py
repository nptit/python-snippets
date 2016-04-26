
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    Write a function called dict_invert that takes in a dictionary with immutable values and returns the inverse of the dictionary. The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. The value for a key in the inverse dictionary is a sorted list of all keys in d that have the same value in d.
    '''
    # Your code here
    from collections import defaultdict
    inv_d = defaultdict(list)
    for k, v in d.items():
        inv_d[v].append(k)

    for k in inv_d:
        inv_d[k].sort()

    return dict(inv_d)

d = {1:10, 2:20, 3:30}
d = {1:10, 2:20, 3:30, 4:30}
d = {4:True, 2:True, 0:True}
d = {8: 6, 2: 6, 4: 6, 6: 6}
print dict_invert(d)
