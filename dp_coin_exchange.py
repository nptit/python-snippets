'''

Given coins of denomination v1=1,v2,v3,v4,...,vn in 
ascending order find minimum number of coins required to make an amount P.
	
C(P) = min {C(P- v[i])} + 1'
'''

def dp_coinexchange(v=[1, 2, 3, 4, 5], P=11):
	C = [0]*(P+1)
	for i in range(1, P+1):
		C[i] = min([C[i-x] for x in v if i >= x]) + 1
	return C[P]

print dp_coinexchange()
