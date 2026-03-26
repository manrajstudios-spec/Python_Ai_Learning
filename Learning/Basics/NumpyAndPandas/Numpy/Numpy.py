import numpy as np

# To Make Numpy Array
array_np = np.array([1,2,3])

print(type(array_np) , array_np)

# multidimensional arrays

np_array = np.array([[[1,2,3],[4,5,6],[7,8,9]],
                     [[10,11,12],[14,15,16],[17,18,19]],
                     [[20,21,23],[24,25,26],[27,28,29]]])

# dimensions and shape
print(np_array.ndim,np_array.shape)

#accessing element
print(np_array[0,0,1]) # 2 # we can use chain indexing too but its too slow using, numpy is faster


# slicing can be done too
print(np_array[::-1]) # reversed

print(np_array[0::2])

#inner elements
print(np_array[0,0,::-1]) # first one reversed

print(np_array[0,:,::3]) # frist from first 

print(np_array[2,:,::3])

print(np_array[:2,::3])

# arithmatic
a_array = np.array([1,2,4])

# doing any operation on numpy array like addition or subract or anything else does that to every other element like add 2 to every element
print(a_array + 2)
print(a_array - 2)
print(a_array / 2)
print(a_array % 2)
print(a_array ** 2)
print(a_array * 2)


#other operations
print(np.round(np.sqrt(a_array))) 

# Two or more arrays
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 * array2)
print(array1 - array2)
print(array1 / array2)
print(array1 % array2)
print(array1 ** array2)

# conditions

array_scores = np.array([100,80,50,90])
print(array_scores == 100)
print(array_scores < 40)

# assinging with conditions

scores = np.array([30,50,60,70,100])
scores = scores[scores < 30]
print(scores)

# Broadcasting

# virtually expanding any array to performs operations on it 
# exapnd in such a way that both array get same size 

# conditions
# the dimensions have same size OR one of them is 1 Example (1,4) and (4,1) OR (4,3) and (1,3)

array_1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array_2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(array_1.shape)
print(array_2.shape)
print(array_1 * array_2)
print((array_1 * array_2).shape) # (10,10)

# array_1 --> (1,10) and array_2 --> (10,1) output becomes (10,10) we expanded 1 to 10 so it becomes (10,10) if we chnages 1 to any other number other than 10 we will get error 


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

# filtering

ages = np.array([[2,3,5,15,16,17,18,89],
                 [14,21,31,13,11,34,54,46]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages <65)]
even = ages[ages %2 == 0]
odds = ages[ages %2 != 0]

print(teenagers)
print(adults)
print(even)
print(odds)

_adults = np.where(ages>= 18 ,ages ,0) # 1 condition 2 array 3 value to set to the element that matches condition
print(_adults) # it keeps the value which follow condition and turn it to 0 if it is False


# random Number 

rng = np.random.default_rng() # we can also seed be putting seed = any number in (seed = n)

print(rng.integers(1,100,(3,2))) # 1 low , 2 high , 3 number of vals needed  for 3 we can also put in a tuple to get 2d 3d or nd array

# matrix multiplication 
# matrix 1 @ matrix b

matrix_array_1 = np.array([[1,2],
                         [3,4]])
matrix_array_2 = np.array([[5,6],
                           [7,8]])

print(matrix_array_1 @ matrix_array_2) # must follow mtrix product rule that is coloumn of first == row of second