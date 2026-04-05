# %% 
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso

# %%
X,y = fetch_california_housing(return_X_y=True)

# %%

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

lrg = Lasso(alpha=0.9)
lrg.fit(X_train,y_train)
lrg.score(X_test,y_test)
# %%
# %%
