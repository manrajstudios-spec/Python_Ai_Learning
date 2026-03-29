# %% 

import matplotlib.pyplot as plt
import numpy as np

#<----------Histo Grams----------->
# They Group Values into bins (intervals) to show distribution of data

# For Histograms Large Number OF Data is Required So
# We'll use Numpy to Genrate Random Values

scores = np.random.normal(loc=80,scale=10,size=100)
#loc is Centre Meanning where do we want our number like around which value we want randome numbers to be
#Scale Is Stardard Deviation And it keep numbers around the value of of 80 deviates only the value mentioned
#Size is number of values

scores = np.clip(scores,0,100) # It Kepps scores between 0 And 100

plt.title("Test Scores" , fontsize=20,fontfamily="Arial",fontweight="bold")

plt.hist(scores,bins=10,color="darkmagenta",edgecolor="black")
plt.xlabel("Scores", fontsize=20,fontfamily="Arial",fontweight="bold")
plt.ylabel("Number Of Students", fontsize=20,fontfamily="Arial",fontweight="bold")

plt.show()


