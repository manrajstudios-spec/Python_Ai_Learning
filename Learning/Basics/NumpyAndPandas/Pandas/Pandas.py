import pandas as pd

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

print(n_series.loc["a"]) #series.loc[label] for accessing using label
print(n_series.iloc[0])#series.iloc[index] for accessing using index

#to change Value at a index 
n_series.loc[1] = 1000#using label
n_series.iloc[2] = 2000#using index
print(n_series)

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

#---------------------------DATA FRAME-------------------------------

#tabular data strucutre rows and coloumn like spreadhseet 2D series

students = {"Name":["Smiley","Angry","Gun",],
            "Age":[16,16,20,],
            }

df = pd.DataFrame(students)
print(df)

#we can have labels too
df_2 = pd.DataFrame(students,index=["Studnet - 1","Student - 2","Student - 3"])

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

#------------------------------- IMPORTING DATA-----------------------------------
r_df = pd.read_csv("Learning/Basics/NumpyAndPandas/pokemons.csv")
print(r_df)

#---> To Read A Json File do (DataFrame = pd.read_json("File Location"))
r_df.to_json("Learning/Basics/NumpyAndPandas/Pokemons_J.json" ,orient="records" , indent=6)

#for all data 
#DataFrame.to_string()
print(r_df.to_string())

# DataFrame.head(n) --> gives the data from start and n is number of rows we want 
print(r_df.head(10))

# DataFrame.tail(n) --> Shows Data From Last and n is number of rows we want
print(r_df.tail(10))

#return info of specific colomns

print(r_df["No"].to_string())
print(r_df["Name"].to_string())
print(r_df["Type1"].to_string())
print(r_df["Type2"].to_string())
print(r_df["Legendary"].to_string())

#print multiple colmns
print(r_df[["Name","Height","Weight"]].to_string())

#get rows
#with index (iloc for index)
print(r_df.loc[2]) # if there are labels then , to access with labels use loc if no labels then loc will give results based on indexes

#to selelect from 1 to n
print(r_df.iloc[:11])

# To Add A setp
print(r_df.iloc[:11:2])

#we can also select coloumns
print(r_df.iloc[:11,:3])

# NOTE To Access Different Colomns With Name We Need To Do .loc not .iloc


#-------------------To Add Labels------------------- 
# We Can Set Any Coloumn As Label So Adding Lables can be easy and we can accesss any row based on name

df_specific = pd.read_csv("Learning/Basics/NumpyAndPandas/pokemons.csv" , index_col=["Name"])# pd.read_csv("file",index-col = [coloumn we want as label])

print(df_specific)

# Lets Try to find Charmander
print(df_specific.loc["Charmander", ["Height","Weight"]])

#to access elements from one to other
#like from charmander to pickachu
print(df_specific.loc["Charmander":"Pikachu",["Type1","Type2"]])

#---------------------------FILTERING-----------------------------------

poke_df = pd.read_csv("Learning/Basics/NumpyAndPandas/pokemons.csv",index_col= ["Name"])

#Example we want separate Pokemons Based on Their Type
#Lets Take All Pokemons With Type1 == "Water" | Type2 == "Water"

fire_df = poke_df[(poke_df["Type1"] == "Water") | (poke_df["Type2"] == "Water")]
print(fire_df)


#<-----------------AGGREGATIONS----------------------->

# --> Used to reduce set of values into a single summerized value
# --> used to analyze Data
# --> groupby() func 

poke_df = pd.read_csv("Learning/Basics/NumpyAndPandas/pokemons.csv",index_col= ["Name"])

print(poke_df.mean(numeric_only=True)) # numeric_only=True means only those coloumns will aloowed who have numeric val
print(poke_df.sum(numeric_only=True))
print(poke_df.max(numeric_only=True))
print(poke_df.min(numeric_only=True)) 
print(poke_df.count()) # it counts number of we can say elements but dont count null vals like Type 2 result is 67

# We can also do this for different coulmns
# Example lets get mean height 

print(poke_df["Height"].mean())

#------------USING GROUP BY--------------

group = poke_df.groupby("Type1")

print(group["Height"].mean()) # We Get AVG Height Of Each Group Based n Type 1# all Other operations work too


#<----------Data Cleaning---------->
# --> Process of removing or fixing wrong data

poke_dex = pd.read_csv("Learning/Basics/NumpyAndPandas/pokemons.csv")

# --> Using df.drop(colomn)

poke_dex = poke_dex.drop(columns=["Legendary","No"])

print(poke_dex)

# Handle Missing Data
# --> df.dropna(subset = [Coloumns We Need To Check]) NOTE --> It will remove the row which have null value for the coloumn mentioned 
# Example --> Like Charmander is pure fire type so Type2 == null , SO if we include Type 2 in subset so charmander row will be dropped

poke_dex = poke_dex.dropna(subset=["Type2"])

print(poke_dex.to_string())

# To Repalce Null values With Something
# We Use df.fillna({"Coloumn_Name":"What We Need To Have Instead of Nan"})

poke_dex = poke_dex.fillna({"Type2":"Don't Have Another Type"}) # We Can Include Other coloumns too by adding more elments to dict
print(poke_dex.to_string())

# TO REPLACE INCONSISTANT VALUES OR WE CAN SAY CHANGE INSTANCES OF PARTICULAR VALUES
# For Example lets change Grass --> GRASS

poke_dex["Type1"] = poke_dex["Type1"].replace({"Grass":"GRASS",           
                                             "Fire":"FIRE"})
print(poke_dex["Type1"]) # We Have GRASS instead of grass AND FIRE Instead of Fire

# Standarize Text

poke_dex["Name"] = poke_dex["Name"].str.lower() # --> Change Every Name To lower Case

# Data Types

poke_dex["Legendary"] = poke_dex["Legendary"].astype(bool) # --> chnages 0 = False , 1 = True

# Remove Duplicates 
# For Example i added multiples instances of bulbasaur
# using df.drop_duplicates() they will be removed

poke_dex = poke_dex.drop_duplicates()

print(poke_dex.to_string()) 