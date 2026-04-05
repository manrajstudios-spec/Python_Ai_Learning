# %%

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %%

df = pd.read_csv("C:/Users/manra_reeinmj/OneDrive/Desktop/Python_Ai_Learning/Learning/MachineLearning/Hour_Score.csv")

# %%
df

# %%

# Lets Visualize
sns.scatterplot(x='Hours' , y="Scores",data=df)

# %%

# CALCS TOTAL LOSS
def Loss_Function(m,c,points):
    tottal_error = 0

    for i in range(len(points)):
        x = points.iloc[i].Hours
        y = points.iloc[i].Scores

        tottal_error += (y - (m*x + c)) ** 2

    return tottal_error/float(len(points)) 

# %%

def gradient_descent(m_now,c_now,L,points):

    grad_m = 0
    grad_c = 0

    for i in range(len(points)):
        x = points.iloc[i].Hours
        y = points.iloc[i].Scores

        error = y - (m_now * x + c_now)

        grad_m += x * error * (-2/len(points))
        grad_c += error * (-2/len(points))

    m = m_now - L * grad_m
    c = c_now - L * grad_c

    return m , c

# %%

def Train(L,epochs,points):
    m = 0
    c = 0

    for i in range(epochs):
        m , c = gradient_descent(m,c,L,points)
        if i % 50 == 0:
            print(f"Current {i}")
            print(f"Loss is {Loss_Function(m,c,df)}")

    print(m,c)

    plt.scatter(df.Hours,df.Scores)

    plt.plot(list(range(2,10)) , [m*x + c for x in range(2,10)])
    plt.show()
# %%
Train(0.0001,2000,df)
# %%
