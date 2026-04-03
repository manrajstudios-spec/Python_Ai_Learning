# %%

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


#%%
df = load_breast_cancer(as_frame=True).frame

# %%
df

# %%

X,y = load_breast_cancer(return_X_y=True)

# %%
X_train , X_test ,y_train ,y_test = train_test_split(X,y,test_size=0.2)

# %%
scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

# %%

# Lets use KNN

from sklearn.neighbors import KNeighborsClassifier 
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier

# WE Can Use Any 3 of the above for classification type problem We just need to replace the below 
clf = KNeighborsClassifier()# to use Linear Regression write LinearRegression in Place of KNeighbour Classifier and same for dicsionTree


clf.fit(X_train_scaled,y_train)

# %%
# TO CHECK SCORE Or We can Say how well modle was trained

clf.score(X_test_scaled,y_test)

# %%

# TO Predict weather person have cancer on not we use predict

# Lets take a rando value from test dataset

to_predict = X_test_scaled[10]
to_predict
# %%

clf.predict([to_predict]) # We Get 1 An we can check real value from y_test as below
# %%
y_test[10] # WE Get 1 


# %%

# clf.predict_proba it gives probability that how much outcome is 0 or 1

clf.predict_proba([to_predict])

# %%
