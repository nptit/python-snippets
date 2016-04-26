__author__ = 'qxu'

'''
# flatmap
from itertools import chain, imap
def flatmap(f, items):
    return chain.from_iterable(imap(f, items))

def flatten(lst):
	return sum( ([x] if not isinstance(x, list) else flatten(x)
		     for x in lst), [] )

def flatten(lst):
     for x in lst:
         if isinstance(x, list):
             for x in flatten(x):
                 yield x
         else:
             yield x

# read text file in blocks using regular expression
import re
result = re.findall(
    r"""(?mx)           # multiline, verbose regex
    ^ID:.*\s*           # Match ID: and anything else on that line
    Name:\s*(.*)\s*     # Match name, capture all characters on this line
    FamilyN:\s*(.*)\s*  # etc. for family name
    Age:\s*(.*)$        # and age""",
    subject)

# read text file in blocks using groupby
import itertools
def isa_group_separator(line):
    return line == '\n'

with open('data_file') as f:
    for key,group in itertools.groupby(f, isa_group_separator):
        # print(key,list(group))  # uncomment to see what itertools.groupby does.
        if not key:
            data={}
            for item in group:
                field,value=item.split(':')
                value=value.strip()
                data[field]=value
            print('{FamilyN} {Name} {Age}'.format(**data))

            # Y X 20
            # F H 23
            # Y S 13
            # Z M 25


from itertools import groupby
with open('your_file') as fin:
    lines = (line.strip('-=\n') for line in fin)
    blocks = [list(g) for k, g in groupby(lines, bool) if k]
    # [['19.37/2', '19.52/2', '21.07/1', '21.22/1', '21.37/1'], ['19.37/2', '19.52/2']]

#If you don't need the data all at once, then make blocks a generator instead and loop over that....

blocks = (list(g) for k, g in groupby(lines, bool) if k)
for block in blocks:
    # do something
'''

def flatmap(l):
    # flatten nested list l
    for item in l:
        if isinstance(item, list):
            for i in flatmap(item):
                yield i
        else:
            yield item

e = [0, [[[1, 2, 3], ['a', 'b'], ['4', ['5', '6']]]]]
list(flatten(e))

mytext='''
=================
19.37/2
19.52/2
21.07/1
21.22/1
21.37/1
-------
19.37/2
19.52/2
-------
'''

lines = (l.strip("-=\n") for l in mytext.split("\n"))
[list(g) for k, g in groupby(lines, bool) if k]
