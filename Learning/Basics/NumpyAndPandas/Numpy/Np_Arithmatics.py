import numpy as np

# arithmatic
a_array = np.array([1,2,4])

# doing any operation on numpy array like addition or subract or anything else does that to every other element like add 2 to every element
# NOTE like dding or subract or any other operation is done with each element

print(a_array + 2)
print(a_array - 2)
print(a_array / 2)
print(a_array % 2)
print(a_array ** 2)
print(a_array * 2)

#other operations
print(np.round(np.sqrt(a_array))) # we can do rounding and find square Root 

array = np.array([[1,3,4,5,6],
                 [3,4,6,856,567]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array)) # standard deviation
print(np.var(array)) # variation
print(np.min(array))
print(np.max(array))
print(np.argmin(array)) # position of minimum val
print(np.argmax(array)) # position of maximum val

# sum rows and coloumns
print(np.sum(array,axis=0))
print(np.sum(array,axis=1))

# Two or more arrays
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 * array2)
print(array1 - array2)
print(array1 / array2)
print(array1 % array2)
print(array1 ** array2)

# matrix multiplication 
# matrix 1 @ matrix b

matrix_array_1 = np.array([[1,2],
                         [3,4]])
matrix_array_2 = np.array([[5,6],
                           [7,8]])

print(matrix_array_1 @ matrix_array_2) # must follow mtrix product rule that is coloumn of first == row of second