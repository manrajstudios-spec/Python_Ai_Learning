# %% 

import matplotlib.pyplot as plt
import numpy as np

#<-------------Scatter Plots----------->

# They Tell The Relation between 2 Things we can say arrays 

# Lets Take Example For Study Hours Increase Marks Increase 

x1 = np.array([0,1,2,2,3,4,5,6,6,7]) # Study Hours
y1 = np.array([40,50,60,65,70,80,85,90,95,98]) # Marks

x2 = np.array([0,1,2,3,4,4,4,8,8,10]) # Study Hours
y2 = np.array([20,30,50,60,65,70,75,80,92,100]) # Marks

plt.title("Relation Of Marks With Study Hours",fontsize=20,fontweight="bold",fontfamily="Arial",color="navy")

plt.xlabel("Study Hours",fontsize=15,fontfamily="Arial",fontweight="bold",color="black")
plt.ylabel("Marks",fontsize=15,fontfamily="Arial",fontweight="bold",color="black")

plt.scatter(x1,y1,color="darkmagenta",alpha=0.7,s=50,label="Class A")
plt.scatter(x2,y2,color="magenta",alpha=0.7,s=50,label="Class B")
# aplha is visibilty of dots
# s is size of dots 

plt.legend() # Shows Label For Different Clases
plt.show()