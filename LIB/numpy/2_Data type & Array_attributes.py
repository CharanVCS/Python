import numpy as np

l= [1, 3, 4, 2]
a1 = np.array(l)
print(a1, a1.dtype) # To check the data type of a NumPy array

# Creating NumPy Arrays With a Defined Data Type
a2 = np.array(l, dtype='int16')
print(a2, a2.dtype)

# type convertion 
int_array = np.array([1, 3, 5, 7])

# convert data type of int_array to float
float_array = int_array.astype('float')

print(int_array, int_array.dtype)
print(float_array, float_array.dtype)

#-> Array attributes
# attributes are properties of NumPy arrays that provide information about the array's shape, size, data type, dimension, and so on.
print(a2.ndim)              
print(a2.shape)
print(a2.size)
print(a2.dtype)
print(a2.itemsize) # it gives memeroy size(inbytes) of element in array
print(a2.data) # it gives memeroy location of array