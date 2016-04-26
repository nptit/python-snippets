
def calculate(s):
    '''given a string of valid expression, evaluate its value'''
    import re
    input = re.split(r'([+|-|*|/])', s.replace(' ', ''))
    stack = []
    for el in stack:
        if el in ['+', '-']:

        elif el in ['*', '/']:
            a = stack.pop
        else:
            stack.append(el)


calculate('2+3*4/2')
