import numpy as np

#Broadcasting allows numpy to perform operation on arrays
#with different shapes by virtually expanding dimensions
#so they match the larger array's shape

#The dimensions have the same size
#OR
#One of the dimensions has a size of 1

arr1 = np.array([[1, 2, 3, 4]])
arr2 = np.array([[1], [2], [3], [4]])

print(arr1.shape)
print(arr2.shape)

print(arr1 * arr2)



#python broadcasting.py

