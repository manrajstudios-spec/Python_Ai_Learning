# %%

import matplotlib.pyplot as plt
import numpy as np

x = np.array([100,200,300,400])
y1 = np.array([2,5,3,0])
y2 = np.array([4,3,1,-1])

# plt.plot(x,y)


#---- Adding Marker ----

# For Conveninece lets make dict For line styles 

line_style = dict(marker = ".",
                markersize = 30,
                mfc = "cyan",
                mec = "black",
                linestyle = "solid",
                linewidth = 2,
                color = "red")

line_style2 = dict(marker = ".",
                markersize = 30,
                mfc = "cyan",
                mec = "black",
                linestyle = "solid",
                linewidth = 2)

#so while plotting we can pass in dict
# To Actually use that dict we need to unpack it using **dict
# To Have different properties we need to remove the property from style and pass in that property while plotting
# in line_style2 theres no color property so we need to pass in color while plotting or else the color will be default

plt.plot(x,y1,**line_style) 
plt.plot(x,y2,color="lime",**line_style2)                               

#line styels
# markeredgecolor == mec and it chnages edge color of marker
# markerfacecolor == mfc so we can use mfc
# solid , dashed , dotted , dashdot , None(for not line connecting markers)
# color is for line color

plt.show()
