import numpy as np

# first we need to creat Numpy Array to perfrom any operation
# create a list named list1
Even = [1.5, 2, 4, 6, 8]

#1->create numpy array using list
array1 = np.array(Even)

# run and observe the difference between list and numpy array 
print("List:",Even)
print(type(Even))
print("numpy array1:",array1)
print(type(array1))

#2->creating of array with 4 zeros
array2 = np.zeros(4)
print("\nnumpy array2:",array2)

# Similarly we can use np.ones() to create an array filled with values 1.

#3->create an array with values from 0 to 4
array3 = np.arange(5)

print("\nUsing np.arange(5):", array3)

# create an array with values from 1 to 8 with a step of 2
array4 = np.arange(2, 9, 2)
print("\nUsing np.arange(2, 9, 2):",array4)

# 4->Create an Array With np.random.rand()
array5 = np.random.rand(2, 3)
array6 = np.random.randint(5, size=4)
print("\nRandom Array:",array5)
print("\nRandom Array:",array6)


# 5->Create an empty Numpy Array 
array7 = np.empty(4)
print("\nEmpty Array",array7)
