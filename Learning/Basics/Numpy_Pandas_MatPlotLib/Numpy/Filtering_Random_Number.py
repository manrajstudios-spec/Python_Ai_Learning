import numpy as np

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