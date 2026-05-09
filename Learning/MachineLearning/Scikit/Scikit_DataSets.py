# %%

from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import seaborn as sns
# %%

df = load_breast_cancer(as_frame=True).frame
df

# %%

for l in df.columns:
    sns.histplot(x = l,hue='target',kde=True,data=df)
    plt.title("Cancer")
    plt.xlabel(l)
    plt.ylabel("Probaility")
    plt.legend()
    plt.show()

# %%

X , y = load_breast_cancer(return_X_y=True)

y

# %%

# MAKE 
import numpy as np

from sklearn.datasets import make_blobs

_X,_y = make_blobs(n_samples=5000,centers=5)

plt.scatter(_X[:,0],_X[:,1],c=_y)
plt.show()
# %%
