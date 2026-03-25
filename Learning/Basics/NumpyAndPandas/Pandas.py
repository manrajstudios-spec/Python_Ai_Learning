import pandas as pd
"""

#-------------SERIES-----------------------------

#series is just a single column like data in single colomn of spreadsheet (1D)

# nomal 
numbers = ["A","B","C","D",10]

series = pd.Series(numbers)

print(series)

#labels changing 

nums = [1,2,3,4]
series_n = pd.Series(nums , index=['a','b','c','d']) 
print(series_n)



#accesing values using labels
n_nums = [60,70,50,20,100]

n_series = pd.Series(n_nums , index = ["a","b","c","d","e"])

# print(n_series.loc["a"]) #series.loc[label] for accessing using label
# print(n_series.iloc[0])#series.iloc[index] for accessing using index

# #to change Value at a index 
# n_series.loc[1] = 1000#using label
# n_series.iloc[2] = 2000#using index
# print(n_series)

#filtering
series_filetered = n_series[n_series > 50]
print(series_filetered)
print(n_series[n_series > 20])

#making series using dictionary

scores = {"Maths":80,
         "Physics":50,
         "Chemistry":60,
         "CS":95,
         "English":30
        }

series_d = pd.Series(scores)


print(series_d)

#changing values
series_d["Maths"] -= 10

print(series_d.loc["Maths"])
print(series_d.loc["Chemistry"])
print(series_d.loc["Physics"])

#filtering

failed = series_d[series_d < 70]
print(failed)

"""

#---------------------------DATA FRAME-------------------------------

#tabular data strucutre rows and coloumn like spreadhseet 2D series

students = {"Name":["Smiley","Angry","Gun",],
            "Age":[16,16,20,],
            }

df = pd.DataFrame(students)
print(df)

#we can have labels too
df_2 = pd.DataFrame(students,index=["Studnet - 1","Student - 2","Student - 3"])
"""
print(df_2)

print(df_2.loc["Student - 3"])
print(df_2.iloc[2])

df_2.iloc[2] = {"Name":"Johan",
           "Age":17}
df_2.loc["Student - 2"] = {"Name":"Daniel",
                           "Age":16}
print(df_2)

print(df_2.loc["Student - 3"])
print(df_2.iloc[2])

print(df_2.loc["Student - 2"])
print(df_2.iloc[1])
"""
#Add New Coloumn 

df_2["Class"] = ["Class 9" , "Class 10" , "Class 11"]
print(df_2)

#Add New Row
# Make New Data Frame Then Concatitnate existing and new one

new_row = pd.DataFrame({"Name":"Jack","Age":17,"Class":"Class 11"} , index= ["Student - 4"])
df_2 = pd.concat([df_2,new_row])
print(df_2)

# For More Than 1 Rows 
new_rows = {"Name":["Silver","Mira"],
            "Age":[17,16],
            "Class":["Class 11","Class 11"]}

new_rows_df = pd.DataFrame(new_rows,index = ["Student - 5","Student - 6"])

new_df = pd.concat([df_2,new_rows_df]) # We Could Have Used Older Data Frame Too
print(new_df)


