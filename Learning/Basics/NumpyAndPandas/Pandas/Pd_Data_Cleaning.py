import pandas as pd

#<----------Data Cleaning---------->
# --> Process of removing or fixing wrong data

poke_df = pd.read_csv("Learning/Basics/NumpyAndPandas/pokemons.csv")

# --> Using df.drop(colomn)

poke_df = poke_df.drop(columns=["No"])

print(poke_df)

# Handle Missing Data
# --> df.dropna(subset = [Coloumns We Need To Check]) NOTE --> It will remove the row which have null value for the coloumn mentioned 
# Example --> Like Charmander is pure fire type so Type2 == null , SO if we include Type 2 in subset so charmander row will be dropped

poke_df = poke_df.dropna(subset=["Type2"])

print(poke_df.to_string())

# To Repalce Null values With Something
# We Use df.fillna({"Coloumn_Name":"What We Need To Have Instead of Nan"})

poke_df = poke_df.fillna({"Type2":"Don't Have Another Type"}) # We Can Include Other coloumns too by adding more elments to dict
print(poke_df.to_string())

# TO REPLACE INCONSISTANT VALUES OR WE CAN SAY CHANGE INSTANCES OF PARTICULAR VALUES
# For Example lets change Grass --> GRASS

poke_df["Type1"] = poke_df["Type1"].replace({"Grass":"GRASS",           
                                             "Fire":"FIRE"})
print(poke_df["Type1"]) # We Have GRASS instead of grass AND FIRE Instead of Fire

# Standarize Text

poke_df["Name"] = poke_df["Name"].str.lower() # --> Change Every Name To lower Case

# Data Types
poke_df = poke_df.drop_duplicates()
poke_df["Legendary"] = poke_df["Legendary"].astype(bool) # --> changes 0 = False , 1 = True

# Remove Duplicates 
# For Example i added multiples instances of bulbasaur
# using df.drop_duplicates() they will be removed

poke_df = poke_df.drop_duplicates()

print(poke_df.to_string())

# SORTING

#LETS Sort By Height

print(poke_df.sort_values(by="Height",ascending=False))