# %% 

import matplotlib.pyplot as plt
import numpy as np

#<----------Pie Charts------------>

# Lets Take An Example Fruits Favoured By People
# Fruits => Apple , Banana , Mango , Watermelon , Gava , Kivi 

fruits = ["Apple","Banana","Mango","Watermelon","Kivi"]
percentage = np.array([6, 13, 19, 21, 41])
colors= ["red","blue","lime","yellow","pink"]

plt.title("Fruits Favoured By People",fontsize=20,fontfamily="Arial",color="black",fontweight="bold")

plt.pie(percentage,labels=fruits,autopct="%1.1f%%",colors=colors,explode=[0,0.2,0,0,0.1],shadow=True,startangle=180) 
# autopct = "%1.1f" gives percentage to each slice based on percentage or data we enetered
# explode = takes slices away from centre
# angle at which chart should start incase we want any category upside

plt.show()
