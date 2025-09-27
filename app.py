import numpy as np


# print(np.__version__) for printing version


arr = [[1, 2, 3, 4], [5, 6, 7, 8]] #this is python list
ara = np.array([1, 2, 3, 4, 5]) #this is numpy array

# #how list and array is printed
# print("List: ", arr)
# print("Numpy Array: ", ara)

# #printing type
# print(type(arr))
# print(type(ara))

#list and numpy array behaves differently
arr = arr * 2 #list element is duplicated. list length doubled
ara = ara * 2 #each element is multiplied by 2

# #printing complete list or array
# print(arr)
# print(ara)

arr0d = np.array('A') #prints only an element
arr1d = np.array([1, 2, 3, 4]) #prints a row
arr2d = np.array([[1, 2, 3], [2, 4, 6], [1, 4, 9], [4, 8, 12]])

# #printing array dimensions
# print(arr0d.ndim)
# print(arr1d.ndim)
# print(arr2d.ndim)

# #printing array shape, number of elements in every dimension should follow same sequence
# print(arr2d.shape)


# # printing element in both list and numpyArray
# print(arr[0][0])
# print(arr2d[0, 0])


# #slicing in numpy
# {
# #print array from ith index to (j-1)th index. print(array[i: j: step])
# print(arr2d[1:4])

# #printing in reverse
# print(arr2d[::-1])

# #printing first 2 row
# print(arr2d[::2])

# #select all rows and access column 0
# print(arr2d[:, 0])

# #select all rows and access 2nd last column
# print(arr2d[:, -2])

# #printing ith to (j-1)th column
# print(arr2d[:, 0:3])

# #print every 2nd column starting from first one
# print(arr2d[:, ::2])

# #print every 2nd column starting from 2nd one
# print(arr2d[:, 1::2])

# #printing first 2 column and first 2 rows
# print(arr2d[0:2, 0:2])

# # printing last 2 column and last 2 rows
# print(arr2d[2:, 1:])
# }


# #scalar Arithmetic operations on array

# #prints all elment with summing 2 to each of them
# print(arr2d+2)

# #prints all elment with substracting 1 to each of them
# print(arr2d-1)

# #prints all elment with multiplying 3 to each of them
# print(arr2d*3)

# #prints all elment with dividing each of them with 4
# print(arr2d/4)

# #prints square root of each element in the array
# print(np.sqrt(arr2d))

# #prints with powering each with 5
# print(arr2d ** 5)

# #rouding each element of the array
# print(np.round(arr2d))

# #using floor ceil
# print(np.floor(arr2d))
# print(np.ceil(arr2d))



# #vectorized math functions
# arr = np.array([1, 2, 3])

# print(np.sqrt(arr))


# #printing value of pie
# print(np.pi)

# ##Exercise of vectorised math functions. given radius. print area of each

# radii = np.array([1, 2, 3])
# print(np.pi * (radii ** 2))


# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# print(arr1 + arr2)
# print(arr1 - arr2)
# print(arr1 * arr2)
# print(arr1 / arr2)
# print(arr2 ** arr1)


#Comparison operators
scores = np.array([91, 55, 100, 73, 82, 64])

print(scores >= 60)

scores[scores < 60] = 0
print(scores)










