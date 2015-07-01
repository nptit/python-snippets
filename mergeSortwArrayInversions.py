def bruteCountInv(arr):
    '''
    counting number of inversions by brute force
    input: a list of integers from [1 to n]
    output: integer, number of inversions
    complexity: O(n)
    '''
    n=len(arr)
    ninv=0
    for i in xrange(n):
      for j in xrange(i,n):
        if arr[i]>arr[j]:
          ninv=ninv+1
    return ninv

def readArr(filename):
    '''
    read a file into an array, each line has one number
    input: filename
    output: an array
    '''
    with open(filename,'r') as f:
	data=f.readlines()
    return [int(x) for x in data]

def splitArray(arr):
    '''
    split an array into half
    input: one array
    output: two arrays of equal length or their lengths differ by one
    '''
    mid=len(arr)//2
    return arr[:mid],arr[mid:]

def mergeSort(arr):
    '''
    preform merge sort 
    input: an array
    output: an array in increasing order
    '''
    if len(arr)<=1:
       return arr
    larr,rarr=splitArray(arr)
    larr=mergeSort(larr)
    rarr=mergeSort(rarr)
    return merge(larr,rarr)

def merge(arr1,arr2):
# merge two sorted arr in O(n) time
    n1=len(arr1)
    n2=len(arr2)
    i1=0
    i2=0
    newarr=[0]*(n1+n2)
    for i in xrange(n1+n2):
      if i1<n1 and i2<n2:
        if arr1[i1]>arr2[i2]:
           newarr[i]=arr2[i2]
           i2=i2+1
        else :
           newarr[i]=arr1[i1]
           i1=i1+1
      elif i1>=n1: # arr1 is exhausted, copy remaining of arr2
        newarr[i]=arr2[i2]
        i2=i2+1
      elif i2>=n2:
        newarr[i]=arr1[i1]
        i1=i1+1
    return newarr

def mergeSortCountInv(arr):
    '''
    preform merge sort, and count number of inversions in an array
    input: an array
    output: an array in increasing order, and # of inversions 
    '''
    if len(arr)<2: 
      return arr,0
    larr,rarr=splitArray(arr)
    larr,lcount=mergeSortCountInv(larr)
    rarr,rcount=mergeSortCountInv(rarr)
    result,splitcount=mergeCount(larr,rarr)
    return result, lcount+rcount+splitcount

def mergeCount(arr1,arr2):
    '''
    merge two sorted arr and count number of inversions in O(n) time
    input: two sorted arrays
    output: one sorted arrays and inversion counts
    '''
    n1=len(arr1)
    n2=len(arr2)
    i1=0
    i2=0
    count=0
    newarr=[0]*(n1+n2)
    for i in xrange(n1+n2):
      if i1<n1 and i2<n2:
        if arr1[i1]>arr2[i2]:
           newarr[i]=arr2[i2]
           i2=i2+1
           count=count+n1-i1
        else :
           newarr[i]=arr1[i1]
           i1=i1+1
      elif i1>=n1: # arr1 is exhausted, copy remaining of arr2
        newarr[i]=arr2[i2]
        i2=i2+1
      elif i2>=n2:
        newarr[i]=arr1[i1]
        i1=i1+1
    return newarr,count
    

# main program
arr=readArr('IntegerArray.txt') # result 2407905288
print len(arr)
#print brute(arr)
arr1=[4,5,3,8,1,2,4]
arr2=[3,4,5]
arr3=[1,2,6]
print "merge sort: ",  arr1
print mergeSort(arr1)
print "merge: ",  arr2, arr3
print merge(arr2,arr3)

arr4=[4,1,3,2,9,1]

print mergeSortCountInv(arr4)
x,count=mergeSortCountInv(arr)
assert (count==2407905288)
