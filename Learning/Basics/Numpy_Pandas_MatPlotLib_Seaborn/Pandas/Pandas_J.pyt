# %% 

import pandas as pd
import numpy as np

# %%

# Series 

nums = np.array([100,200,300,400,500])

s = pd.Series(nums)
s

# %%

#LABELS

s = pd.Series(nums,index=['a','b','c','d','e'])

s
# %%

# DATA FRAME

df = pd.DataFrame({"Name":["Jay","Gun","Jack","Johan","Goo"],
                   "Age":[17,19,17,16,19],
                   "Class":[10,12,10,10,12]
                    }
                )
df
                   
# %%

# SET INDEX

df = df.set_index(['Name'])
df
# %%

# ACCESS

df.loc['Jay']
# %%
df = df.reset_index()

# %%

# EXPORT DATA FRAME

df.to_csv("Learning/Basics/Numpy_Pandas_MatPlotLib_Seaborn/Pandas/test_Data.csv",index=None)
# %%

df_r = pd.read_csv("Learning/Basics/Numpy_Pandas_MatPlotLib_Seaborn/Pandas/test_Data.csv")

df_r
