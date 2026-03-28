import numpy as np
import pandas as pd

"""
#<--------------------Numpy---------------------->

array = np.array([[[1,2,3],[4,5,6],[7,8,9]],
                  [[10,11,12],[13,14,15],[16,17,18]],
                  [[19,20,21],[22,23,24],[25,26,27]]])

# --> BASICS
print(array.ndim)
print("------------------------------")
print(array.shape)
print("------------------------------")
print(array[0,1,2])

print("------------------------------")
print("------------------------------")

print(array[::-1])
print("------------------------------")
print(array[:,1])
print("------------------------------")
print(array[0,::-1])

print("------------------------------")
print("------------------------------")

# --> ARITHMATICS

a = np.array([2,4,6])
print(a + 5)
print("------------------------------")
print(a ** a)
print("------------------------------")
print(a / 2)

print("------------------------------")
print("------------------------------")

x = np.array([1,2,3])
y = np.array([4,5,6])

print(x * y)
print("------------------------------")
print(x-y)
print("------------------------------")
print(x ** y)

print("------------------------------")
print("------------------------------")

# --> DATA CHECKING

arr = np.array([10,20,30,40,50])

print(arr[arr > 25])
print("------------------------------")
print(arr[arr % 2 == 0])
print("------------------------------")
print(arr == 30)

print("------------------------------")
print("------------------------------")
print(np.where(arr >= 30 , arr , 0))

print("------------------------------")
print("------------------------------")

# --> BROADCASTING

m = np.array([[1,2,3,4]])
n = np.array([[1],[2],[3],[4]])

print(m * n)
print("------------------------------")
print((m*n).shape)

# --> AGGREGATIONS

array_arr = np.array([[1,2,4],
                       [5,6,7],
                       [7,8,9]])

print(array_arr.sum())
print("------------------------------")
print(array_arr.mean())
print("------------------------------")
print(array_arr.min())
print("------------------------------")
print(array_arr.max())
print("------------------------------")
print(array_arr.argmin())
print("------------------------------")
print(array_arr.argmax())
print("------------------------------")
print(array_arr.sum(axis = 0))
print("------------------------------")
print(array_arr.sum(axis = 1))

# --> FILTERING

ages = np.array([[10,15,20],[25,30,35]])

print(ages[ages < 18])
print("------------------------------")
print(ages[(ages > 18) & (ages < 30)])
print("------------------------------")
print(ages[ages % 2 != 0])

"""

data = {
    "Name": ["Aman", "Riya", "Kabir", "Simran", "Arjun", "Riya", "Kabir"],
    "Age": [17, 18, 19, np.nan, 20, 18, 19],
    "Marks": [85, 90, 78, 88, np.nan, 90, 78],
    "Class": ["10", "12", "11", "10", "12", "12", "11"],
    "City": ["Delhi", "Mumbai", "Delhi", "Punjab", "Mumbai", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data,index=["Aman","Riya","Kabir","Simran","Arjun","Riya","Kabir"])

print(df.head(3))
print("------------------------------")
print(df.tail(2))

print("------------------------------")
print("------------------------------")

print(df.loc["Riya"])
print("------------------------------")
print(df.iloc[2])

print("------------------------------")
print("------------------------------")

print(df[df["Marks"] > 80])
print("------------------------------")
print(df[df["City"] == "Delhi"])
print("------------------------------")
print(df[(df["Marks"] > 80) & (df["City"] == "Mumbai")])

print("------------------------------")
print("------------------------------")

print(df.notna())

print("------------------------------")
df = df.fillna({"Marks":df["Marks"].mean()})
df = df.fillna({"Age":df["Age"].median()})
print(df)


print("------------------------------")
print("------------------------------")

df = df.drop_duplicates()
df["Name"] = df["Name"].str.lower()
print(df)

print("------------------------------")
print("------------------------------")

lst = []

for m in df["Marks"]:
    if m > 80:
        lst.append(True)
    else:
        lst.append(False)

df["Coloumn"] = lst
print(df)

print("------------------------------")
print("------------------------------")

group = df.groupby("City")

print(group["Marks"].mean())