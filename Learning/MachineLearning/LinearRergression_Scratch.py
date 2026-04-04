# %%

import pandas as pd
import seaborn as sns

# %%

df = pd.read_csv("Learning/MachineLearning/Hour_Score.csv")

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

        tottal_error += y - (m*x - c) ** 2

    tottal_error/float(len(points)) 

# %%

def gradient_descent(m_now,c_now,L,points):

    grad_m = 0
    grad_c = 0

    for i in range(len(points)):
        x = points.iloc[i].Hours
        y = points.iloc[i].Scores

        grad_m += x * (y - (m_now * x + c_now))
        grad_c += (y - (m_now * x + c_now))

    m = m_now - L * (-grad_m * 2) /len(points)
    c = c_now - L * (-grad_c * 2) /len(points)

    return m , c

# %%

def Train(L,epochs,points):
    m = 0
    c = 0

    for i in range(epochs):

        if i % 50 == 0:
            print(f"Current {i}")
        m , c = gradient_descent(m,c,L,points)

    print(m,c)

    sns.scatterplot(x='Hours' , y="Scores",data=df)

    sns.lineplot(list(range(20,80)) , [m*x + c for x in range(20,80)])

# %%
