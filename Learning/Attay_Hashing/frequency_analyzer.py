from array import array

nums = array('i',[1,2,2,3,3,4,5,6,6,6,7,7,5])
mores = {}

def Check(num:int):
    times = 0

    for n in nums:
        if n == num:
            times += 1
    return times

for n in nums:
    mores[n] = Check(n)


print(mores)

# other way

more_n = {}
for n in nums:
    if n in more_n:
        more_n[n] += 1
    else:
        more_n[n] = 1
print(more_n)

# other way

more_n_n = {}
for n in nums:
    more_n_n[n] = more_n_n.get(n,0) + 1

print(more_n_n)