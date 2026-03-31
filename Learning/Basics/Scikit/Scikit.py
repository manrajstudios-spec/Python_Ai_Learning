# %%

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


# %%

# LOADS DATASET IN DATA FRAME
data = load_breast_cancer(as_frame=True).frame

data

# %%

# TO SPLI IN X AND Y
# X --> Features
# y --> Outcome

X, y = load_breast_cancer(return_X_y=True)
X
y
# %%

# Now Spliit Dataset into X_train and X_test AND  y_train and y_test

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2)

# %%
# NOW Scale Data

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

# %%
