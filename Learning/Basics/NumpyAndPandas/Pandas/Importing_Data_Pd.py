import pandas as pd

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