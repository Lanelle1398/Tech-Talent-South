import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    b=numpy.array(arr, float)
    return (b[::-1] ) 

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
