import numpy as np

A = np.array([1, 3, 5])
B = np.array([0, 2, 3])

# union of two arrays
result = np.union1d(A, B) # (A U B) operation
print(result)
 
# intersection of two arrays
result = np.intersect1d(A, B) #(A ∩ B) operation
print(result)  

# difference of two arrays
result = np.setdiff1d(A, B) #(A - B) operation
print(result)  

# symmetric difference of two arrays
result = np.setxor1d(A, B)
print(result) 

# -->
array1 = np.array([1,1, 2, 2, 4, 7, 7, 3, 5, 2, 5])

# unique values from array1
result = np.unique(array1)
print(result)  
