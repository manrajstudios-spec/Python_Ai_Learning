# %% 

from sklearn.datasets import make_blobs,make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans ,DBSCAN

# %%
X,y = make_blobs(n_samples=5000,centers=5,random_state=10)

scalar = StandardScaler()

X_scaled = scalar.fit_transform(X)

# %%

import matplotlib.pyplot as plt


plt.scatter(X_scaled[:,0],X_scaled[:,1])

# %%


# USING KMeans

kmeans = KMeans(n_clusters=5)

kmeans.fit(X_scaled)
# %%

plt.scatter(X_scaled[:,0],X_scaled[:,1],c=kmeans.labels_)
# %%
plt.scatter(X_scaled[:,0],X_scaled[:,1],c=y) # TO CHECK


# %%

# DBSCAN

dbscan = DBSCAN()

X , y = make_moons(n_samples=5000,noise=0.0.7)

X_scaled = scalar.fit_transform(X)

plt.scatter(X_scaled[:,0],X_scaled[:,1])

# %%
