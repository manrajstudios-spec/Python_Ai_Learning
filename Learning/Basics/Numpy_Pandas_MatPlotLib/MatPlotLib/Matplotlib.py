import matplotlib.pyplot as plt
import numpy as np
x = np.array([100,200,300,400])
y = np.array([2,5,3,-1])

# plt.plot(x,y)

#---- Adding Marker ----
plt.plot(x,y,marker = ".",markersize= 10,markerfacecolor="cyan")

plt.show()
