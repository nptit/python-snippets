__author__ = 'qxu'


a=[[1,2],[3,4]]
b=[[1,2,3],[4,5,6],[7,8,9]]

def rotate2(mat):
    n = len(mat)
    nmat=[]
    for i in xrange(n):
        row=[]
        for j in xrange(n):
            row.append(mat[j][i])
        nmat.append(row[::-1])
    return nmat

def rotate(mat):
    return zip(*mat[::-1])

print rotate(a)
print rotate(b)