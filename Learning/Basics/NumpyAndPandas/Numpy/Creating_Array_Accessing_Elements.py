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

print(np_array[0,:,::3]) # first from first 

print(np_array[2,:,::3])

print(np_array[:2,::3]) 

# Accessing elements with conditions 

scores = np.array([100,70,20,40,60,80])
print(scores>50)#NOTE --> [it sets values matching condtion to true and others to Fales]


