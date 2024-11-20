import numpy as np

array1d = np.array([2, 4, 6, 8, 1, 3, 5, 7])
print("1d array:\n", array1d)

# Reshaping to 2d array
array2d = np.reshape(array1d, (2, 4)) #it will reshape (2, 4) - 2 rows and 4 columes
print("2d array:\n", array2d)

#Reshaping to 3d array
array3d = np.reshape(array1d, (2, 2, 2)) #it will reshape (2, 2, 2) - 2 widths 2 rows and 2 columes
print("3d array:\n", array3d)

# Flattening a matrix simply means converting a matrix into a 1D array.
arrayf = array3d.flatten()

if np.array_equal(array1d, arrayf): 
    print(arrayf)