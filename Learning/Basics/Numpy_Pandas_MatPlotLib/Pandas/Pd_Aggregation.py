import pandas as pd

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