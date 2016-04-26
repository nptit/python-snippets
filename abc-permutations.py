from itertools import product

mask = product([0, 1], repeat=3)
d = dict((i, c) for i, c in enumerate('abc'))
for m in mask:
	print tuple(d[i] if e else '*' for i, e in enumerate(m))