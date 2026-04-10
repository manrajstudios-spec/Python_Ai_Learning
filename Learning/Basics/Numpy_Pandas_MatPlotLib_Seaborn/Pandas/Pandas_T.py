# %% 
import pandas as pd
from sklearn.datasets import load_breast_cancer

# %%

df = load_breast_cancer(as_frame=True).frame

# %%

df

# %%

df.target = (df['target'] ==1).astype(bool)

# %%
df

# %%

df.columns
# %%
df.columns[:-1]
# %%

# GET VALUES OF COLOUMNS

df.iloc[:,:-1]
# %%
# DIFF WAY 

df.loc[:,df.columns != 'target']
# %%
