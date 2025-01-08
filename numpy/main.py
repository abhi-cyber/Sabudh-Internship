# Numpy :-
'''
1. Less storage space required
2. Fixed type
3. Contiguous memory (data stored in order and not scattered)
4. Allows to do operations between arrays 
5. MATLAB (Mathematical operations)
6. Used as backend for Pandas
7. Used Plotting Graphs (Matplotlib)
8. Unlike list you can make arrays in 1D, 2D, 3D and so on.
'''

import numpy as np

a = np.array([1,2,3]) # 1-D
print(a)

b = np.array([[1,2,3],[4,5,6]]) # 2-D
print(b)

# Get Dimension
print(a.ndim)
print(b.ndim)

# Get Shape
print(a.shape)
print(b.shape)

# Get Type
print(a.dtype)
print(b.dtype)

c = np.array([1,2,3], dtype='int16') # Defining data type
print(c.dtype)

# Get Item Size
print(a.itemsize)
print(c.itemsize)

# Get Total Size
print(b.nbytes)
print(c.nbytes)

# Accessing / Changing Elements


d = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(d)
print(d[0,0]) # Accessing element at position (0,0)
print(d[0,:]) # Accessing all elements of a specific row. Visa versa in case of entire specific column

# [start index, end index, stepsize]
print(d[0,1:6:2]) # Accessing elements of a specific row with step size of 2

# Matrix of all zeros
print(np.zeros((2,3)))

# Matrix of all ones
print(np.ones((2,3)))

# Matrix of all specific number
print(np.full((2,2), 99)) # takes 2 parameters, shape and number. It can take dataType as a parameter too.

# Random Int Matrix
print(np.random.randint(10,size=(2,2)))

# Identity Matrix (Digonal elements are 1's and rest are 0's)
print(np.identity(5)) # 5 here is the dimension 5 x 5

''' Note :-  Be careful when coping arrays cause if in case you set 'a = b' and then update the array 'b', 
similarly 'a' will also get updated. '''

# Linear Algebra

a1 = np.ones((2,3))
a2 = np.full((3,2), 2)

print(np.matmul(a1,a2)) # Matrix Multiplication

# Find the determinant
a3 = np.identity(3)
print(np.linalg.det(a3)) # Determinant of a matrix

# You can perform Stastics on the array in np
a4 = np.random.randint(10,size=(2,2))
print(np.min(a4))
print(np.max(a4))
print(np.sum(a4))

# Reorganizing Arrays
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((8,1)) # Reshaping the array
print(after)

# Vertically stacking vectors

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack((v1,v2)))

# Horizontal stacking vectors
print(np.hstack((v1,v2)))

# Load data from file
data = np.genfromtxt('./data.txt', delimiter=',')
print(data)