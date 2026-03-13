import time

#-------------list-----------
"""
name = str(input("Enter Your Name: "))
age = int(input("Enter Your Age: "))
Gender = str(input("Enter Your Gender: "))
address = input("Enter Your Adress: ")

User_Data = [name, age ,Gender, address]

print(User_Data)

print(User_Data)
User_Data[1] += 20"""

#------------List slicing-------------------
"""
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

"""
"""
fruits = ["apple","mango","banana" , "grape"]
fruitsNotWantingToEat = ["apple","banana"]
print(fruits)

for i in fruits:
    for j in fruitsNotWantingToEat:
        if i == j:
            fruits.remove(i)

print(fruits)
"""

#------------Arrays-------------
import array

numbers = array.array('i' ,[0,2,3,4,5])

nums = numbers[::-1]
print(nums)
nums = numbers[0:6:2]

for i in numbers:
    if(i==3):
        numbers.pop(i)

print(numbers)

#----------touple----------------
#just unchangeable list 
"""
numbers = (1,2,3,4)
data = ("Manraj" , 17,"Male")
#cannot be changed

#for touple with one element add a comma otherwise it will think it is a just a str or int or float or double

singleElement = (5,) """