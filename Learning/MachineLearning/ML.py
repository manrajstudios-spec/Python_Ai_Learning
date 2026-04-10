# %%
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("/home/manraj_studios/Python/Python_Ai_Learning/Learning/MachineLearning/magic04.csv")

# %%
df
# %%
coloumns = ["fLength","fWidth","fSize","fConc","fConc1","fAsym","fM3Long","fM3Trans","fAlpha","fDist","class"]

df.columns = coloumns
# %%
df['class'] = (df['class'] == 'g').astype(bool).astype(int)
df
# %%
for label in df.columns:
    plt.hist(df[df['class'] ==1][label] , color = 'red' , label = 'g' , alpha=0.7)
    plt.hist(df[df['class'] ==0][label] , color = 'blue' , label = 'h' , alpha=0.7)
    plt.legend()
    plt.show()
# %%

# TRAIN TEST VALID

train,valid,test = np.split(df.sample(frac=1) , [int(0.6* len(df)) , int(0.8 * len(df))])
# %%
def Scale_Dataset(dataframe,oversample=False):
    X=dataframe[:,:-1]
    y=dataframe[:,-1]
    
    scalar = StandardScaler()
    X=scalar.fit_transform(X)

    if oversample:
        ros = RandomOverSampler()
        X,y = ros.fit_resample(X,y)
    
    data = np.hstack((X,np.reshape(y,(-1,1))))
    return data,X,y
# %%
train , X_train,y_train = Scale_Dataset(dataframe=train,oversample=True)
valid , X_valid , y_valid = Scale_Dataset(valid,False)
test , X_test , y_test = Scale_Dataset(test,False)
# %%

# KNN
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)

print(classification_report(y_test,knn.predict(X_test)))
# %%