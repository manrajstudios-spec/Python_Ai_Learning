# %%

import seaborn as sns

# %%

# DataSets
tips = sns.load_dataset("tips")
titanic = sns.load_dataset("titanic")
iris = sns.load_dataset("iris")
planets = sns.load_dataset("planets")

# %%
# SCATTER PLOT
tips
sns.scatterplot(x='tip',y='total_bill',data=tips,hue="day",palette="YlGnBu") # hue divides data based on provided
# For Example above without hue data shows tips with total bill but with hue on day it will divide the info between days 


# %%
# BAR PLOT

tips
sns.barplot(x='sex',y='tip',data=tips,hue='smoker')

# %%
# HIST PLOT

sns.histplot(tips['tip'],bins=15,kde=True) # kde is distribution curve of data

# %%
#DISTRIBUTUON Plot

sns.displot(tips["tip"],kde=True)

# %%

# Box Plot

sns.boxenplot(x='day',y='tip',data=tips,hue='sex')
# %%
# STRIP PLOT

sns.stripplot(x='day',y='tip',data=tips,hue='sex',dodge=True) # dodge separate hue condtions
# %%
# Joint Plots

sns.jointplot(x='tip',y='total_bill',data=tips,kind='hex')
# %%

# PAIR PLOTS

titanic
sns.pairplot(titanic.select_dtypes(['number']),hue='pclass')

# %%
titanic.corr(numeric_only=True)
sns.heatmap(titanic.corr(numeric_only=True),annot=True,cmap='icefire')