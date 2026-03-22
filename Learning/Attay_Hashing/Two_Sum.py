from array import array

nums = array('i',[2,7,11,17])
target = 9

seen = {}

for i,n in enumerate(nums):
    f = target - n
    if f in seen:
        print(f"Number 1 : {n} at index --> {i} , Number 2 : {f} at index --> {seen[f]}")
        break
    else:
        seen[n]  = i