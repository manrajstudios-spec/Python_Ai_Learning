import random
"""
name = str(input("Enter Your Name Here: "))
age = int(input("Enter your Age Here: "))

print("Your Name is: " + name)
print("Your Age is: " + str(age))

if(age < 18):
    print("Your Are Minor")
else:
    print("You are fucking adult")"""

rand_number = random.randint(0,10)
user_Guess = (input("Enter Your Guess Here: "))

if(str(user_Guess) == ""):
    user_Guess = 0

print("Random Number is: " + str(rand_number))
print("Your Guess is: " + str(user_Guess))
if(user_Guess == rand_number):
    print("you Won the Game")
else:
    print("You Noob You Lost: ;)")
