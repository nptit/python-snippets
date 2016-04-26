# -*- coding: utf-8 -*-
# 
'''
Moving Average Jan 6 2015
要求实现对于一个window_size， 不停插入值，返回当前的平均数，
如果输入没有达到window_size则输出所有数的平均值，达到后踢掉最早的输入输出最新的平均值。
例子：
For Window size: 2
MovingAverage m(2)
m.get_next(1) -> 1
m.get_next(2) -> 1.5
m.get_next(3) -> 2.5
m.get_next(4) -> 3.5
'''

class MovingAverage(object):
	def __init__(self, window_size=2):
		self.data = []
		self.window_size = window_size

	def __iter__(self):
		return self

	def next(self, value):
		self.data.append(value)

		if len(self.data) < self.window_size:
			return sum(self.data)/float(len(self.data))
		else:
			data = self.data[-self.window_size:]
			return sum(data)/float(self.window_size)


x = MovingAverage(window_size=2)
print x.next(1)
print x.data
print x.next(2)
print x.data
print x.next(3)
print x.next(4)