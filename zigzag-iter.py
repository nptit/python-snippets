# -*- coding: utf-8 -*-
'''
Zigzag Iterator Jan 30 2015
写一个变形的iterator，给定两个iterator，让两个iterator进行交互输出。
例子：
A: 1234
B: abcd
则输出为：1a2b3c4d，如果一个读完了那就读没读完那个直到两个都读完为止。
G家电面题，又是iterator系列。很简单，但是尽量写的容易扩展一些，因为interviewer很可能会让你扩展到k个iterator的情况。
'''


a = '1234'
b = 'abcd'

print ''.join([''.join(c) for c in zip(a,b)])


import itertools

b = 'abcde'
print [c for c in itertools.izip_longest(a,b)]


def zigzag_funct(a, b):
	lena, lenb = len(a), len(b)
	min_len = min(lena, lenb)
	ret = []
	for i in xrange(min_len):
		ret.extend([a[i], b[i]])

	if lena > lenb:
		ret.extend(a[min_len:])
	else:
		ret.extend(b[min_len:])

	return ret

print zigzag_funct(a, b)


def zigzag_generator(a, b):
	lena, lenb = len(a), len(b)
	min_len = min(lena, lenb)
	for i in xrange(min_len):
		yield a[i]
		yield b[i]

	if lena > lenb:
		for i in a[min_len]:
			yield i
	else:
		for i in b[min_len]:
			yield i


x = zigzag_generator(a, b)
print list(x)


class zigzag_class(object):
	def __init__(self, a, b):
		lena, lenb = len(a), len(b)
		min_len = min(lena, lenb)
		ret = []
		for i in xrange(min_len):
			ret.extend([a[i], b[i]])

		if lena > lenb:
			ret.extend(a[min_len:])
		else:
			ret.extend(b[min_len:])

		self.data = ret
		self.index = 0

	def __iter__(self):
		return self

	def next(self):
		if self.index >= len(self.data):
			raise(StopIteration)
		else:
			self.index += 1
			return self.data[self.index-1]

x = zigzag_class(a, b)
print "x= ", list(x)
