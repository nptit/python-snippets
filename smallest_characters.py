'''
Smallest Chatacter Feb 10 2015
Given a sorted character array and a character, return the smallest character that is strictly larger than the search character.

If no such character exists, return the smallest character in the array.

For example:

Input: ['c', 'f', 'j', 'p', 'v'], 'a'
Output: 'c'

Input: ['c', 'f', 'j', 'p', 'v'], 'c'
Output: 'f'

Input: ['c', 'f', 'j', 'p', 'v'], 'z'
Output: 'c'

Input: ['c', 'c', 'k'], 'f'
Output: 'k'
'''

# conventional 

'''
import bisect


def smallest_character(arr, target):
	index = bisect.bisect_left(arr, target)
	return arr[index] if index<len(arr) else arr[0]


def smallest_character(arr, target):
	if target <= arr[0] or target >= arr[-1]:
		return arr[0]

	middle_index = len(arr) // 2

	if target >= arr[middle_index]:
		return smallest_character(arr[middle_index:], target)
	else:
		return smallest_character(arr[:middle_index], target)
'''


def smallest_character(arr, target):
	l, r, ret = 0, len(arr) - 1, arr[0]
	while l <= r:
		m = (l + r) // 2
		if arr[m] > target:
			r = m - 1
			ret = arr[m]
		else:
			l = m + 1
	return ret



a = ['c', 'c', 'c', 'c', 'd','f', 'k']
t = 'f'
print "t4= ", smallest_character(a, t)




a = ['c', 'f', 'j', 'p', 'v']
t = 'a'
print "t1= ", smallest_character(a, t)

a = ['c', 'f', 'j', 'p', 'v']
t ='c'
print "t2= ", smallest_character(a, t)

a = ['c', 'f', 'j', 'p', 'v']
t = 'z'
print "t3= ", smallest_character(a, t)


