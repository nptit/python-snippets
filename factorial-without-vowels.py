# Write a function named "e_fecterel" which calculates the factorial without using these letters in code: "aiou".

def e_fecterel(n):
    return n*e_fecterel(n-1) if n>=1 else 1


print e_fecterel(4)
