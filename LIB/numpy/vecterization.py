import numpy as np

# array whose square we need to find
array1 = np.array([-1, 0, 2, 3, 4])

# function to find the square
def find_square(x):
    if x < 0:
        return 0
    else:
        return x ** 2
        
# vectorize() to vectorize the function find_square()
vectorized_function = np.vectorize(find_square)

# passing an array to a vectorized function
result = vectorized_function(array1)

print(result)