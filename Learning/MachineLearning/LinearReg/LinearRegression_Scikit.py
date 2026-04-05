# %% 
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# %%
X,y = fetch_california_housing(return_X_y=True)

# %%
lrg = RandomForestClassifier(n_estimators=200)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

lrg.fit(X_train,y_train)

# %%
