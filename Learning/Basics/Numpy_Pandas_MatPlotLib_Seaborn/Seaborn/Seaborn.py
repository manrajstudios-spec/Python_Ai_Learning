# %%

import seaborn as sns

# %%

# DataSets
tips = sns.load_dataset("tips")
titanic = sns.load_dataset("titanic")
iris = sns.load_dataset("iris")
planets = sns.load_dataset("planets")

# %%
tips
sns.scatterplot(x='tip',y='total_bill',data=tips,hue="day",palette="YlGnBu")

# %%
tips
sns.barplot(x='sex',y='tip',data=tips,hue='day')
# %%
sns.histplot(tips['tip'],bins=15,kde=True) # kde is distribution curve of data
sns.displot(tips["tip"],kde=True)


# %%
