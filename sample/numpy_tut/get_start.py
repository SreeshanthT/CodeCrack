import numpy as np

a = np.array(43)



"""
2-D Array

An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.
"""
b = np.array([[1,2,3],[4,5,6]])


"""
3-D Array

An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor.
"""
a = np.array([b, b])
# print(a)
# print(a.ndim)

"""
Higher Dimensional Arrays
An array can have any number of dimensions.

When the array is created, you can define the number of dimensions by using the ndmin argument.
"""
a = np.array([1, 2, 3, 4], ndmin=5)
# print(a)
# print(a.ndim)

"""
Access Array Elements
Array indexing is the same as accessing an array element.

You can access an array element by referring to its index number.

The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.
"""
arr = np.array([[1,2],[3,4]])
# print(arr.ndim)

for i in range(arr.ndim):
    for j in range(arr.ndim):
        print(f"arr[{i}][{j}] = {arr[i][j]}")

        
# print(arr[1][0])