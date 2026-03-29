import pandas as pd

#---------------------------FILTERING-----------------------------------

poke_df = pd.read_csv("Learning/Basics/NumpyAndPandas/pokemons.csv",index_col= ["Name"])

#Example we want separate Pokemons Based on Their Type
#Lets Take All Pokemons With Type1 == "Water" | Type2 == "Water"

fire_df = poke_df[(poke_df["Type1"] == "Water") | (poke_df["Type2"] == "Water")]
print(fire_df)