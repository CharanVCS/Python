import numpy as np

a1 = np.array([1, 2, 3, 4, 5])

# np.save("file1.npy", a1) #it stores data as binary 
# load() - loads data from a binary file in the NumPy .npy format

np.savetxt("file.npy", a1) # it stores data as text in current directory
a2 = np.loadtxt("file.npy") # loadtxt() reads the values as floating point numbers by default.
print(a2)

# -->
# Array Indexing in 2D array - it is same as list
array= np.array([[1, 3, 5, 7], [2, 4, 6, 8]])
print('\n2d array:', array)

# To access the row elememts in 2d array
print('2nd row elements:', array[1, :])
# To access the colume elements in 2d array
print('3rd coloum in array:', array[:, 2])

# Array Slicing is also same as string slicing
# for 1d array - array[start:stop:step]
# for 2d array - array[row_start:row_stop:row_step, col_start:col_stop:col_step]