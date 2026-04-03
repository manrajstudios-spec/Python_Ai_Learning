# %%

from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split , StratifiedShuffleSplit
from sklearn.preprocessing import StandardScaler 

# %%

X,y = load_breast_cancer(return_X_y=True)

split = StratifiedShuffleSplit(n_splits=1,test_size=0.2)

for train_idx , test_idx in split.split(X,y):
    X_train , X_test = X[train_idx] , X[test_idx]
    y_train , y_test = y[train_idx] , y[test_idx]

# %%

scalar = StandardScaler()


X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

# %%
clf = KNeighborsClassifier()

clf.fit(X_train_scaled,y_train)
clf.score(X_test_scaled,y_test)
# %%

from sklearn.metrics import accuracy_score , recall_score , f1_score , precision_score

# %%

# ACCURACY SCROE

y_predict = clf.predict(X_test_scaled)

# %%
accuracy_score(y_test,y_predict)

# %%
recall_score(y_test,y_predict)

# %%
f1_score(y_test,y_predict)

# %%
precision_score(y_test,y_predict)

# %%

# ON REGRESSION TYPE

from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression


# %%

X,y = fetch_california_housing(return_X_y=True)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

# %%
reg = LinearRegression()
reg.fit(X_train_scaled,y_train)

# %%
y_predict = reg.predict(X_test_scaled)

# %% 
reg.score(X_test_scaled,y_test)
# %%

from sklearn.metrics import r2_score , mean_absolute_error , mean_squared_error , root_mean_squared_error


# %%
r2_score(y_test,y_predict)

# %%
mean_absolute_error(y_test,y_predict)

# %%
mean_squared_error(y_test,y_predict)

# %%
root_mean_squared_error(y_test,y_predict)

# %%
