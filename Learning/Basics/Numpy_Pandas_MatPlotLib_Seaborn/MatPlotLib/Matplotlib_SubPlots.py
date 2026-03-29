# %% 

import matplotlib.pyplot as plt
import numpy as np

#<------------Sub Plots------------>

# Two Parts Figure And SubPlots Figure Contains SubPlots

figure,axes = plt.subplots(2,2) # axes is numpy array and plt.sublopts()returns a tuple
# 2,2 Gives 4 subplots means figure is divided in 4 parts and we can have as many or as less as subplots as we need
# (2,1) (1,1) (3,1) any numbers are applicable

# To Plot In Those SubPlots

x1 = np.array([10,20,30,40])
y1 = np.array([2,4,6,8])

x2 = np.array([10,20,30,40])
y2 = np.array([8,6,4,2])

x3 = np.array([10,20,30,40])
y3 = np.array([2,4,2,4])

x4 = np.array([10,20,30,40])
y4 = np.array([1,50,20,50])

axes[0,0].plot(x1,y1,marker=".",mfc="navy",mec="black",markersize=10,color="red")
axes[0,0].set_title("Increasing",fontsize=10,fontfamily="Arial",fontweight="bold") # To add Title to each subPlot we need set_title 

axes[0,1].scatter(x2,y2,alpha=1,s=100,label="XY",color="blue")
axes[0,1].set_title("Decreasing",fontsize=10,fontfamily="Arial",fontweight="bold")

axes[1,0].bar(x3,y3,color="yellow")
axes[1,0].set_title("Increasing & Decreasing",fontsize=10,fontfamily="Arial",fontweight="bold")

axes[1,1].plot(x4,y4,marker=".",mfc="orange",mec="black",markersize=10,color="purple")
axes[1,1].set_title("Variation",fontsize=10,fontfamily="Arial",fontweight="bold")

# Subplots are not limited to line charts only we can have bar charts and scatter charts as above 

plt.tight_layout() # Avoids Overlap
plt.show()