import numpy as np

def create_array(*args):
    n=len(args)
    arr=np.zeros((n,n),dtype=int)
    for i in range(n):
        arr[i][i]=args[i]
    return arr

arr=create_array(1,2,3,4)
print(arr)