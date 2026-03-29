# %% 

import matplotlib.pyplot as plt
import numpy as np

# Lets Make a Random Data for how many laptops sold by ASUS In Different Years

years = np.array([2020,2021,2022,2023,2024])
numbers = np.array([100,200,50,150,300])


plt.title("Laptops Sold by Asus",fontsize=20,fontfamily="Arial",color="black",fontweight="bold")
plt.xlabel("Years",fontsize=20,fontfamily="Arial",color="black",fontweight="bold")
plt.ylabel("Numbers",fontsize=20,fontfamily="Arial",color="black",fontweight="bold")

plt.bar(years,numbers,color="cyan",edgecolor="black")
# plt.barh(years,numbers,color="cyan") # to Make Horizontal Bar Graph plt.barh() is used 

plt.show()