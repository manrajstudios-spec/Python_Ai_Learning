# %% 
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# %%
X,y = fetch_california_housing(return_X_y=True)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)


# %%
from sklearn.linear_model import LinearRegression

reg = LinearRegression()

reg.fit(X_train_scaled,y_train)

# %%
reg.score(X_test_scaled,y_test)

# %%

reg.predict([X_test_scaled[1]])
# %%
y_test[1]
# %%
