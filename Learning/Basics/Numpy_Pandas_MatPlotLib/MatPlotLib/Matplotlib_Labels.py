# %%
import matplotlib.pyplot as plt
import numpy as np 

#<----------Labels---------->

x = np.array([2020,2021,2022,2023,2024])
y1 = np.array([10,20,30,40,50])
y2 = np.array([65,60,52,40,30])
y3 = np.array([70,80,60,90,50])

plt.title("SmartPhone Sold Data",fontsize=20,fontfamily="Arial",fontweight="bold",color="red")

plt.xlabel("Year",fontsize=20,color = "black",fontfamily="Arail",fontweight="bold")
plt.ylabel("Numbers",fontsize=20,color = "black",fontfamily="Arail",fontweight="bold")

plt.plot(x,y1,marker=".",markersize="20",mfc="black",mec="white")
plt.plot(x,y2,marker=".",markersize="20",mfc="black",mec="white",linestyle="dashed")
plt.plot(x,y3,marker=".",markersize="20",mfc="black",mec="white",linestyle="dashdot")

# To Have ticks at only values mean only values in x ar
# Meaning only values in x array will be shown no other values values between two poitns will be shown

plt.xticks(x)

#To change tick colors
plt.tick_params(axis="both" , colors = "brown")# we can change of individual axis too by passing x and y

plt.show()