import time
import array
#-------------list-----------
name = str(input("Enter Your Name: "))
age = int(input("Enter Your Age: "))
Gender = str(input("Enter Your Gender: "))
address = input("Enter Your Adress: ")

User_Data = [name, age ,Gender, address]

print(User_Data)

print(User_Data)
User_Data[1] += 20

#------------list Operations----------------
lst = [1,2,3,4,5]

#append add an element at last 
lst.append(6)
print(lst)

#acces element
print(lst[0])
#insert
lst.insert(1,4) # first value is index and second is value means at index 1 4 is added
print(lst)

#pop
lst.pop(0) #removes element at index 0 or any other value we type in  by Default removes -1th element
print(lst)

#remove

lst.remove(2)  # removes the first occurence of provided value
print(lst)

# lenght of list
i = len(lst)#numbers of elemts
print(i)

#check if elemnts exists in and not in
exists = 1 not in lst
print(exists)

# clear
lst.clear()
print(lst)


#------------List slicing-------------------

numbers = [1,2,3,4,5]

for i in range(1,11):
    if i not in numbers:
        numbers.append(i)
        print(numbers)
        time.sleep(0.2)
    else:
        if i in numbers:
            numbers.remove(i)
            print(numbers)
            time.sleep(0.15)
n = numbers[0:11:2]
print(n)


fruits = ["apple","mango","banana" , "grape"]
fruitsNotWantingToEat = ["apple","banana"]
print(fruits)

for i in fruits:
    for j in fruitsNotWantingToEat:
        if i == j:
            fruits.remove(i)

print(fruits)


#------------Arrays-------------


numbers = array.array('i' ,[0,2,3,4,5])

nums = numbers[::-1]
print(nums)
nums = numbers[0:6:2]

for i in numbers:
    if(i==3):
        numbers.remove(i)
print(numbers)

#array operations
arr = array.array('i' ,[1,2,3,4,5])

#access element
print(arr[2])

#append
arr.append(3)
print(arr)

#insert
arr.insert(2,4)
print(arr)

#remove 
arr.remove(3) # removes first instance of 3
print(arr)

#pop
arr.pop() # by default removes -1th elemnt
print(arr)

#lenght

print(len(arr))

#----------touple----------------
#just unchangeable list 

numbers = (1,2,3,4)
data = ("Manraj" , 17,"Male")
#cannot be changed

#for touple with one element add a comma otherwise it will think it is a just a str or int or float or double

singleElement = (5,) 

#--------------Sets--------------------

# alist where two elemnts cannot be same 

# various operation like union (a|b) intersection (a&b) 

a = {1,2,2}

print(a) # output {1,2} not {1,2,2}


a = {2,4,6,8} 
b = {1,3,5,7}

print(a|b)
print(a-b)#not ordered
print(a & b)

#--------inter conversions----------

#list ----------> array only if list have all elements of same data type

lst = {1,2,3}

arr = array.array("i",lst) #error if list is of different data types
print(arr)

toup = (lst)

print(toup)

st = set(lst)
print(st)

stt = {1,2,3,4,5}

lstt = list(stt)
print(lstt)

arrr = array.array("i",stt)
print(arrr)

touppp = (stt)
print(touppp)

strr = "Manraj"

lsts = list(strr)
print(lsts)

arrs = array.array("u",lsts)
print(arrs[2])