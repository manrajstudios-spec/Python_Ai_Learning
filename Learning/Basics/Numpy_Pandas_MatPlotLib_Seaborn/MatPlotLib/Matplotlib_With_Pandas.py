# %% 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#<------------MatPlotLib With Pandas-------------->

df = pd.read_csv("Learning/Basics/Numpy_Pandas_MatPlotLib/pokemons.csv")

type_count = df["Type1"].value_counts(ascending=True) # tells How many elements have certain type 

plt.barh(type_count.index,type_count.values,color="navy",edgecolor="black")

plt.title("Number Of Pokemons Per Type",fontsize=20,fontfamily="Arial",fontweight="bold",color="black")
plt.xlabel("Pokemons",fontsize=20,fontfamily="Arial",fontweight="bold",color="black")
plt.ylabel("Number Of Pokemons",fontsize=20,fontfamily="Arial",fontweight="bold",color="black")

plt.tight_layout()
plt.show()
