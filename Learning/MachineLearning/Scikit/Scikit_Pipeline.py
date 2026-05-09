# %%
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
# %%
X,y  = load_breast_cancer(return_X_y=True)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

# %%

pipe = Pipeline(
    [('scale',StandardScaler()),
    ('PCA',PCA(n_components=10)),
    ('RFC',RandomForestClassifier(n_jobs=-1))]
)


# %%

pipe.fit(X_train,y_train)
# %%
pipe.score(X_test,y_test)
# %%
