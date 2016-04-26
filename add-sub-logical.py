'''
def plus_num2(a, b):
	while b != 0:
		carry = a & b 
		a = a^b #sum
		b = b << 1
	return a

def sub_num2(a, b):
	while b != 0:
		borrow = (~a) & b 
		a = a^b 
		b = b << 1
	return a
'''

#http://www.geeksforgeeks.org/subtract-two-numbers-without-using-arithmetic-operators/
#http://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/
#https://en.wikipedia.org/wiki/Adder_(electronics)

MAX_BIT = 2**32
MAX_BIT_COMPLIMENT = -2**32

def plus_num(a, b):
    while b != 0:
        if b == MAX_BIT:
            return a ^ MAX_BIT_COMPLIMENT
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a

def sub_num(a, b):
    while b != 0:
        if b == MAX_BIT:
            return a ^ MAX_BIT_COMPLIMENT
        carry = (~a) & b
        a = a ^ b
        b = carry << 1

    return a


print plus_num(5, 5)


print plus_num(-1000, 8000)
print sub_num(-1000, 8000)
