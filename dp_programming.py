''' Given a rod of length N units and price of rods of all sizes from 1 to N,
find the best way of cutting the rod, i.e in how many pieces and of what length
we should cut so that we get maximum price for it. '''

def cut_for_maximum(prices={1:10, 2:5, 3:20, 4:8}, rodlen=10):
	' knapsack problem  C[i] = max( C[i-x] + v[x] for all x<i ) '
	C = [0]*(rodlen+1)
	for i in range(1, rodlen+1):
		C[i] = max([C[i-x] + prices[x] for x in prices if i >= x])
	return max(C[1:])

print cut_for_maximum(prices={1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20}, rodlen=8)


'''
Given a sequence of letters, find the length of the longest Palindromic subsequence.
For example in the sequence XAYBZBA, longest palindromic subsequence is ABZBA which is of length 5

LP(i, j) =

1 if i=j
1 if j=i+1 and x[i] != x[j]
2 if j=i+1 and x[i] == x[j]
LP(i+1, j-1) +2 if x[i] == x[j]
max {LP(i+1, j), LP(i, j-1)}

'''

def longest_palindromic_substr(string='ABZAB'):
	pass
