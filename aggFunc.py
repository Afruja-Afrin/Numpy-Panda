import numpy as np

#Aggregate functions = summarize data and typically return a single value

arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])


print(np.sum(arr)) # sum of array elements
print(np.mean(arr)) # mean of array elements
print(np.std(arr)) # standard deviation of all elements
print(np.var(arr)) # variance of elements
print(np.min(arr)) # minimum element of the array
print(np.max(arr)) # maximum element of the array
print(np.argmin(arr)) # print index of the minimum element
print(np.argmax(arr)) # print index of the maximum element

#printing sum of all columns
print(np.sum(arr, axis = 0))
#printing sum of all row
print(np.sum(arr, axis = 1))









# python aggFunc.py