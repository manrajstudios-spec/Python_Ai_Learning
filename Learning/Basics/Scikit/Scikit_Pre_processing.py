# %% 

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# %%

X , y = load_iris(return_X_y=True)


# %%

# A Scalar is used to scale or centre values around 0 that's what standard scalar does so that to avoid inconsistancies in modle while training


# STANDARD SCALAR

# Lets Split First

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)



# %%

# Now lest Scale

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.fit_transform(X_test)

# %%

# TO DO STANDARD SCALE MANUALLY

import numpy as np

# Subract X_train from its mean per feature and divide by std

(X_train - np.mean(X_train,axis=0))/np.std(X_train,axis=0)


# %%

# MIN MAX SCALING Keeps Vals between 0 and 1 means no vals -ve

from sklearn.preprocessing import MinMaxScaler

scalar_m = MinMaxScaler() # Pushes Between 0 and 1

X_train_scaled_m = scalar_m.fit_transform(X_train)
X_test_scaled_m = scalar_m.transform(X_test)

# Manual Way

X_min = np.min(X_train,axis=0)
X_max = np.max(X_train,axis=0)

# Subrcat min from train then divide by subrcation of max and min

(X_train - X_min)/X_max-X_min

