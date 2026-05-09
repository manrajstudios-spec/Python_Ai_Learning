# %%

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import cross_val_score , StratifiedShuffleSplit
from sklearn.neighbors import KNeighborsClassifier
# %%
X,y = load_breast_cancer(return_X_y=True)

scalar = StandardScaler()

X_scaled = scalar.fit_transform(X)

# %%
clf = KNeighborsClassifier()

scores = cross_val_score(clf,X_scaled,y,cv=5,scoring='precision')
# %%

scores
# %%
import numpy as np

np.mean(scores)
# %%
