# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.array([100,200,300,400,500])
y = np.array([20,50,10,80,30])

#<------Grid----->

plt.grid(axis="y",linewidth=2,color="lightgrey",linestyle="solid") # if want only on x or y type in x or y respectively

plt.plot(x,y,marker=".",markersize=20,mfc="brown",mec="grey",linestyle="dashed",linewidth=2,color="lime")
plt.show()