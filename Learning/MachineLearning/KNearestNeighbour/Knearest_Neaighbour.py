# %% 
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# %%
points = {"blue":[[2,4,3],[1,3,5],[2,3,1],[3,2,3],[2,1,6]],
          "red":[[5,6,5],[4,5,2],[4,6,1],[6,6,1],[5,4,6]]} # TRAINING DATA

new_point = [3,3,4] # WE NEED OUR MODLE TO TELL US WHEATHER THIS POINT IS RED OR BLUE

# %%
def Euclidean_dist(p,q):
    return np.sqrt(np.sum((np.array(p) - np.array(q)) **2))
# %%

class KNearestNeighbours:

    def __init__(self,k=3):
        self.k = k
        self.points = None
    
    def fit(self,points):
        self.points = points
    
    def predict(self,new_point): # NEW POINT IS WHER WE WANT TO PREDICT VAL
        distances = []

        for category in self.points: # WE LOOP THROUGH TRAINING POINTS #NOTE LOOP THROUGH KEYS OF DICT
            for point in self.points[category]: # WE LOOP THROUGH ELEMENTS FOR SPECIFIC CATEGORY
                distance  = Euclidean_dist(point,new_point) # WE CALC DIST OF CUR POINT FROM GIVEN POINT
                distances.append([distance,category]) # THEN APPEND

        categories = [category[1] for category in sorted(distances)[:self.k]] # IN THIS WE WE MAKE LIST OF FIRST K ELEMENTS OF DISTANCES
        result = Counter(categories).most_common(1)[0][0] # IT TELLS WHICH IS MOST COMMON IN FIRST K
        return result
        
# %%
knn = KNearestNeighbours()

knn.fit(points=points)
# %%
print(knn.predict(new_point))
# %%


# VISUALIZE 

fig = plt.figure(figsize=(15,12))
ax = fig.add_subplot(projection='3d')
ax.grid(True,color="grey")
ax.set_facecolor('black')
ax.figure.set_facecolor("black")
ax.tick_params(axis="both",color='white')

for p in points['blue']:
    ax.scatter(p[0],p[1],p[2],color='blue',s=60)

for p in points['red']:
    ax.scatter(p[0],p[1],p[2],color='red',s=60)

n = knn.predict(new_point)

color = 'red' if n == 'red' else 'blue'

ax.scatter(new_point[0],new_point[1],new_point[2],color=color,marker='*',s=200,zorder=100)

for p in points['blue']:
    ax.plot([new_point[0],p[0]] , [new_point[1] , p[1]] ,[new_point[2] , p[2]], color='yellow')

for p in points['red']:
    ax.plot([new_point[0],p[0]] , [new_point[1] , p[1]] ,[new_point[2] , p[2]], color='green',linestyle='--')

plt.show()

# %%
