'''
Programming Interview: Longest Increasing Sub-sequence (Dynamic Programming)
'''

def longest_sub_seq(L):
	# S[i] = S[i-1]+1 if L[i] > L[i] else S[i-1]
	S = [1] * len(L)
	for i in xrange(1,len(L)):
		S[i] = max(S[:i]) + 1 if L[i] > L[i - 1] else 1
	return max(S)

def longest_consecutive_sub_seq(L):
	# continous increasing sub sequence
	S = [1] * len(L)
	for i in xrange(1,len(L)):
		S[i] = S[i-1] + 1 if L[i] > L[i - 1] else 1
	return max(S)



l1 = [1, -1, 3, 2, 3, 4, 2, 5]
print longest_sub_seq(l1)
print longest_consecutive_sub_seq(l1)