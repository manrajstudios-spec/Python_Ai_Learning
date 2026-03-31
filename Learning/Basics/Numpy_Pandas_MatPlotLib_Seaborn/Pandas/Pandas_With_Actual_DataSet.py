# %%
import pandas as pd
from sklearn.datasets import fetch_california_housing

# %%
df :pd.DataFrame = fetch_california_housing(as_frame=True).frame
df
# %%

# HEAD 
df.head(10)

# %%

# TAIL
df.tail(10)

# %%
 
# RANDOM ROW

df.sample(2) # 2 rand rows or any number

# %%

# GET COLOUMNS

cols = list(df.columns)
cols

# %%

# DISPLAY LIMTS

pd.options.display.max_columns = 5

df
# %%

# INFO

df.info()


# %%
# DESCRIBE
df.describe()

# %%

# SPECIFIC COLS

df.HouseAge
df["HouseAge"]
# %%

# Operations

# Exaples df.HouseAge or any other col func mean sum count mode.... etc.

# Graph
import matplotlib.pyplot as plt

df.HouseAge.hist()

plt.hist(x=df["HouseAge"],color='red',alpha=0.6,density=True,label="House Age",edgecolor='black')
plt.title("HOUSE AGE",fontsize=20)
plt.legend()
plt.show()

# %%
df.hist(figsize=(18,12))
plt.tight_layout()

# %%

df_1 = pd.read_csv("Learning/Basics/Numpy_Pandas_MatPlotLib_Seaborn/Pandas/test_Data.csv")
df_1
# %%
