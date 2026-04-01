# %% 
import pandas as pd
# %%

df = pd.DataFrame({'name':["Jay", "Daniel", "Johan", "Jack", "Gun", "Goo", "Kim", "EliJang", "Crystal", "Mira"],
                   "age":[16, 18, 17, 19, 20, 21, 18, 17, 22, 23],
                   "class":[10, 12, 11, 12, 9, 11, 10, 10, 12, 11],
                   "parttime":[1,0,0,1,0,1,0,1,0,1]})

df

# %%

df[df["parttime"] == 1].name

# %%

df[df['age'] > 18]

# %%

import seaborn as sns

sns.histplot(x='age',data=df,hue='parttime')


# %%

# ADD NEW ROW
df.loc[10] = ["Zoey",17,11,1]
df

# %%

df['grades'] = [90,100,30,40,50,20,80,70,80,50,10]

df

# %%

group = df.groupby(df.grades > 50)


# %%
