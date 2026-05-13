'''import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(np.mean(arr))
print(np.sum(arr))'''

'''import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))
print("Biggest:", np.max(arr))
print("Smallest:", np.min(arr))'''

import numpy as np
#Create arrays
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

#Math operations
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

#2D array (like a table)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("Matrix:\n", matrix)

#shape of array
print("Shape:", matrix.shape)

#Range of numbers
r = np.arange(1, 11)
print("Range 1-10:", r)

#Sort an array
unsorted = np.array([5, 2, 8, 1, 9])
print("Sorted:", np.sort(unsorted))
