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

df_1 = pd.read_csv("Learning/Basics/Numpy_Pandas_MatPlotLib_Seaborn/Pandas/test_Data.csv",index_col=0)
df_1

# %%
# ACCESS ELEMENTS

df_1.loc["Jay"]
df_1.loc["Gun"]

# %%
df_1.iloc[0:2]

# %%

df_1.at['Gun',"Age"]
# %%
df_1.iat[1,0]
# %%

# CHANGE VALS

df_1.loc["Gun"] = [20,12]
df_1

# %%
df_1.at["Gun","Age"] = 21
df
df_1
# %%

# DATA CLEANING

df_1.at["Jack","Age"] = float('nan')

df_1.info()

# %%

# DROP NA
df_1 = df_1.dropna()
df_1

# %%

# FILL NA

df_1.loc["Jack"] = [float('nan'),10]
df_1.info()

df_1= df_1.fillna(17)
df_1

# %%

df_1.at["Jack",'Age'] = float('nan')
df_1.at["Jay",'Class'] = float('nan')
df_1
df_1.info()


# %%

df_1[df_1.Age.notna()]

# %%


# ITERATE OVER DATA Rows

for i,row in df_1.iterrows():
    print(row)
    print(row['Class'])
    print(row['Age'])

# %%

# ITERATE OVER COLS

for i , cols in df_1.items():
    print(i) # AGE AND CLASS
    print(cols) # WE get firstly age of all names then class of all names
    print(cols['Gun'])


# %%

# FILTER

df_1.Age > 18 # SHOWS IN TRUE FALSE WHICH IS 18 OR LARGER

# %%
df_1[df_1.Age > 18] # GIVES ANOTHER DF FOR 18 OR OLDER

# %%

df_1[(df_1.Age > 16) & (df_1.Class > 10)]

# %%

df_1[df_1.Class.notna()]
df_1[-df_1.Class.notna()] # MINUS IS LIKE ADDING !

# %%

df_2 = pd.read_csv("Learning/Basics/Numpy_Pandas_MatPlotLib_Seaborn/Pandas/test_Data.csv")
df_2
df_2[df_2.Name.str.endswith('n')]
# %%

import datetime as dt

df_2['BirthDate'] = df_2.Age.apply(lambda x: dt.datetime.now() - dt.timedelta(days = 365*x))
df_2

# %%

df_2[df_2.BirthDate.dt.year > 2007]
# %%

ages = [17]

df_2[df_2.Age.isin(ages)]

# %%

df_2["PartTime"] = [1,1,0,0,0]
df_2
# %%

# AGG find mean of each row 

df_2.groupby('PartTime').agg({"Age":"mean"})
# %%
# LETS TAKE ANOTHER EXAMPLE

new_df = pd.DataFrame({"Name":"Jim",
                    "Age":16,
                    "BirthDate":dt.datetime.now() - dt.timedelta(days = 365*16),
                    "PartTime":1} , index=[5])

df_2 = pd.concat((df_2,new_df))
df_2["FullJob"] = [0,0,1,1,1,0]
df_2


# %%
df_2.groupby('FullJob').agg({"Age":"median"})
# %%

#MERGE AND CONCAT
"""
a = {"Item":["A","B","C","D"],
     "Price":[100,200,30,40]}
b = {"Items":["A","B","C","C"],
     "Price":[20,30,40,40]}

pd.concat((a,b)).reset_index()"""
# %%
