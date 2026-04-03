# %%
from sklearn.datasets import fetch_openml
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# %%
X,y = fetch_openml('mnist_784',return_X_y=True)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2) 
# %%
pca = PCA(n_components=10)

X_train_reduced = pca.fit_transform(X_train)
X_test_reduced = pca.transform(X_test)

# %%

reg = LogisticRegression(max_iter=100)

reg.fit(X_train_reduced,y_train)
reg.score(X_test_reduced,y_test) # WE GET 0.80

# %%
# WITHOUT PCA we get 0.91
reg.fit(X_train,y_train)
reg.score(X_test,y_test)
# %%
