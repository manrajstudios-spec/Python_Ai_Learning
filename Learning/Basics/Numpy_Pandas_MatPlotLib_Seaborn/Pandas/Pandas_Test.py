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

df_n = df.copy()

df_n
# %%

df_n.loc[5:8,'grades'] = float('nan')
df_n

# %%

df_n.drop(5,axis=0)

df_n.drop('class',axis=1)

df_n
# AXIS 1 drops cols and Axis = 0 drops rows but we need to say df = stuff if we dont set it df wont change 


# %%

adults = df[df.age >= 18]
teens = df[df.age < 18]

adults
# %%
employed_adults = df[(df.age >= 18) & (df.parttime == 1)]

employed_adults

# %%

df.groupby('parttime').agg({"age":["mean","min","max","sum"]})

# %%

df.sort_values('age',ascending=False)

# %%

df_1  = pd.DataFrame({"items":["A","B","C","D","E"],
                      "price":[10,20,30,40,50]})

df_2 = pd.DataFrame({"items":["E","F","G","H"],
                     "price":[40,50,60,70]})


# %%

#CONCAT
pd.concat([df_1,df_2]).reset_index().drop('index',axis=1)


# %%

df_3 = pd.DataFrame({'Country':["X","Y","Z"],
                     "available":[True,False,True]})


# %%
# BASICALLY TO STACK BY COLOUMNS
pd.concat([df_1,df_3],axis=1)

# %%

# NOW TO STACK TWO DFS WHICH HAVE SAME COLOUMN WE USE MERGE
pd.merge(df_1,df_2,how="outer")
# %%
