# %% 

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split,StratifiedShuffleSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

# %%
X,y = load_breast_cancer(return_X_y=True)


split = StratifiedShuffleSplit(n_splits=1,test_size=0.2)

for train_i , test_i in split.split(X,y):
    X_train,X_test = X[train_i],X[test_i]
    y_train,y_test = y[train_i],y[test_i]

# %%

params = {
    "n_estimators":[50,100,200],
    "max_depth":[None,5,10],
    "min_samples_split":[2,5]
}

rfc = RandomForestClassifier(n_jobs=-1) # n_jobs -1 tells to use all cpu cores

grid = GridSearchCV(rfc , param_grid=params , cv=3)

grid.fit(X_train,y_train)
# %%
grid.best_params_
# %%
best_rfc = grid.best_estimator_

# %%
best_rfc.score(X_test,y_test)
# %%
