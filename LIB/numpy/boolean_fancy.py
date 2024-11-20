import numpy as np

# create an array of numbers
array1 = np.array([1, 8, 4, 9, 6, 10, 7, 2, 5, 3])
print(array1)

# create a boolean mask
boolean_mask = array1 % 2 != 0

# boolean indexing to filter the odd numbers
result = array1[boolean_mask]
print(result)

# make a copy of the array
numbers_copy = array1.copy()

# change all even numbers to 0 in the copy
numbers_copy[array1 % 2 == 0] = 0
print(numbers_copy)


# --> fancy indexing

# select elements at index 1, 2, 5, 7
select_elements = array1[[1, 2, 5, 7]]
print(select_elements)

# sort array1 using fancy indexing in descending order
sorted_array = array1[np.argsort(-array1)]
print(sorted_array)
