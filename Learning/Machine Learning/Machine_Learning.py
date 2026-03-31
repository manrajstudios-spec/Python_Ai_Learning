# %%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# %%
cols = ["fLength","fWidth","fSize","fConc","fConc1","fAsym","fM3Long","fM3Trans","fAplpha","fDist","class"]

df = pd.read_csv("magic04.data",names=cols)
df['class'] = (df['class'] == 'g').astype(int)
df


# %%

for label in cols[:-1]:
    plt.hist(df[df['class'] == 1][label] , density=True,alpha= 0.5,color='blue',label='gamma')
    plt.hist(df[df['class'] == 0][label] , density=True,alpha= 0.5,color='red',label='hadron')
    plt.title(label)
    plt.xlabel(label)
    plt.ylabel("Probability")
    plt.legend()
    plt.show()


# %%
# TRAIN VALID SPLIT
train,valid,split = np.split(df.sample(frac=1) , [int(0.6 * len(df)),int(0.8 * len(df))])


# %%

def scale_dataset(dataframe):
    X = dataframe[dataframe.cols[:-1]].values
    y = dataframe[dataframe.cols[-1]].values
    
    scalar = StandardScaler()
    X = scalar.fit_transform(X)

    data = np.hstack((X,np.reshape(y,(-1,1))))
    return data,X,y

