import numpy as np

# Broadcasting

# virtually expanding any array to performs operations on it 
# exapnd in such a way that both array get same size 

# conditions
# the dimensions have same size OR one of them is 1 Example (1,4) and (4,1) OR (4,3) and (1,3)
# it chekc from right to left like 10 X 1 and 1 X 10 it will check the right side one with right side 10 first

array_1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array_2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(array_1.shape)
print(array_2.shape)
print(array_1 * array_2)
print((array_1 * array_2).shape) # (10,10)

# array_1 --> (1,10) and array_2 --> (10,1) output becomes (10,10) we expanded 1 to 10 so it becomes (10,10) if we chnages 1 to any other number other than 10 we will get error 
