import time
import math
'''
for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("hey yo")

'''
'''
for i in range(50,100+1,2):
    print(i)

for i in "Manraj Singh":
    print(i)'''

row = 5
coloumn = 5

for i in range(row):
    for j in range(coloumn):
        print("*" , end="")      
    print()
#-------empty sqaure-------
""" 
for i in range(row):
    for j in range(coloumn):
        if i==0 or i ==row-1:
            print("*",end="")
        else:
            if j == 0 or j == coloumn-1:
                print("*",end="")
            else:
                print(" " , end="")
    print()"""

#---------right triangle right side---------
"""
for i in range(5):
    for dash in range(5+(-i-1)):
        print(" ",end="")
    for star in range(i+1):
        print("*",end="")
    print()"""

#--------up right pyramid---------
"""
for i in range(4):
    star = 2*i+1
    dash = 7-star
    for dash1 in range(int(dash/2)):
        print("_" , end="")
    for asterisks in range(star):
        print("*" , end="")
    for dash1 in range(int(dash/2)):
        print("_" , end="")
    print()

for i in range(4):
    print("_" * (4-i-1) + "*" * (2*i-1))"""

#------reverse pyramid---------
"""
for i in range(4):
    star = 7-2*i
    dash = 7 - star

    for dash1 in range(int(dash/2)):
        print("_" , end="")
    for asterisks in range(star):
        print("*" , end="")
    for dash1 in range(int(dash/2)):
        print("_" , end="")
    print() """

#------diamond-------
"""

for i in range(3):
    star = 2*i+1
    dash = 7-star
    for dash1 in range(int(dash/2)):
        print("_" , end="")
    for asterisks in range(star):
        print("*" , end="")
    for dash1 in range(int(dash/2)):
        print("_" , end="")
    print()
for i in range(4):
    star = 7-2*i
    dash = 7 - star

    for dash1 in range(int(dash/2)):
        print("_" , end="")
    for asterisks in range(star):
        print("*" , end="")
    for dash1 in range(int(dash/2)):
        print("_" , end="")
    print() 
"""

