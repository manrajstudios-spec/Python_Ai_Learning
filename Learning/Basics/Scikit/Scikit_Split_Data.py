# %% 

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


# %%

df = load_iris(as_frame=True).frame
df.columns

# %%
X,y = load_iris(return_X_y=True)

X

# %%
y

# %%

# TRAIN TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2) # 0.2 means 20% of data is for testing and 80% = Training

# %%

# NOW LET US Shuffle data so we get a ideal ratio of each outcome

from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1,test_size=0.2)

for train_idx,test_idx in split.split(X,y): # WHAT THIS DOES IS EACH OUTCOME IS CORRECTLY DISTRIBUTED IN ALL SPLITS
    X_train , X_test = X[train_idx] , X[test_idx]
    y_train , y_test = y[train_idx] , y[test_idx]

# %%

# This show that sometimes instance of one outcome may differ in test and train like 
# if we get 0 10 times and 1 only 3 times in train and while testing we will face inconsistancies which will lead to a greater loss
import numpy as np
import matplotlib.pyplot as plt

count = np.bincount(y_train)
positions = np.arange(3)

plt.bar(positions,count)
plt.xticks(df['target'])

# %%

count = np.bincount(y_test)
positions = np.arange(3)

plt.bar(positions,count)
plt.xticks(df['target'])

# %%
