import pandas as pd

#---------------------------DATA FRAME-------------------------------

#tabular data strucutre rows and coloumn like spreadhseet 2D series

students = {"Name":["Smiley","Angry","Gun",],
            "Age":[16,16,20,],
            }

df = pd.DataFrame(students)
print(df)

#we can have labels too
df_2 = pd.DataFrame(students,index=["Student - 1","Student - 2","Student - 3"])

print(df_2)

print(df_2.loc["Student - 3"])
print(df_2.iloc[2])

df_2.iloc[2] = {"Name":"Johan",
           "Age":17}
df_2.loc["Student - 2"] = {"Name":"Daniel",
                           "Age":16}

#<----------------- Access Elements------------->

# iloc and loc 
#.iloc or .loc[row ,coloumn] when have multiple coloumn Data Frame

#lets print Student - 3's Name And Age 

print(df_2.loc[["Student - 3"] , ["Name","Age"]])

print(df_2.loc["Student - 2"])
print(df_2.iloc[1])

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
