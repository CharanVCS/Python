import numpy as np

# create two matrices
mtx1 = np.array([[1, 3], [5, 7]])
mtx2 = np.array([[2, 6], [4, 8]])
print(mtx1, mtx2)

# calculate the dot product of the two matrices
result = np.dot(mtx1, mtx2)
print("mtx1 x mtx2: \n",result)

# get transpose of mtx1
result = np.transpose(mtx1)
print(result)
# Alternatively, we can use the .T attribute to get the transpose of a matrix.

# find inverse of mtx1
result = np.linalg.inv(mtx1)
print(result)

# find determinant of matrix1
result = np.linalg.det(mtx1)
print(result)

# Flattening a matrix simply means converting a matrix into a 1D array.
result = mtx1.flatten()
print("flattened mtx1", result)
